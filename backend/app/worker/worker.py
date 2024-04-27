import asyncio
import datetime
import json
import logging
import os
from collections import namedtuple

import requests
from celery import Celery
from celery import chain
from langchain_community.document_loaders import PyPDFLoader
from app.db import prisma
import trafilatura

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from app.config.config import ML_SERVICE_URL

prisma.prisma_client.connect()

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")

@celery.task(name="create_text_workflow")
def plan_for_text(text: str):
    return chain(text_extraction.s(text), model_invocation.s()).delay()


@celery.task(name="create_url_workflow")
def plan_for_url(url: str):
    return chain(url_extraction.s(url), model_invocation.s()).delay()


@celery.task(name="create_pdf_workflow")
def plan_for_pdf(text: str):
    return chain(pdf_extraction.s(text), model_invocation.s()).delay()


@celery.task(name="pdf_extraction")
def pdf_extraction(file_path: str) -> str:
    pdf_loader = PyPDFLoader(file_path)
    pages = pdf_loader.load()
    text = ""
    for page in pages:
        text += page.page_content

    logger.debug(f"extracted text from {file_path}: {text}")
    return json.dumps({
        "title": f"some_vacancy_from_pdf: {text}"
    })

@celery.task(name="save_request")
def save_request(): {

}

@celery.task(name="url_extraction")
def url_extraction(url: str):
    extracted_text = parse_html(url)
    return extracted_text


@celery.task(name="text_extraction")
def text_extraction(text: str) -> str:
    return json.dumps({
        "title": f"some_vacancy_from_text: {text}"
    })


@celery.task(name="model_invocation")
def model_invocation(vacancy_ser: str) -> int:
    request_to_save = {
        "request": vacancy_ser,
        "performed_at": datetime.datetime.now()
    }

    request_to_save = prisma.prisma_client.modelrequest.create(request_to_save)
    response_to_save = {
        "request_id": request_to_save["id"],
        "started_at": datetime.datetime.now()
    }
    response_to_save = prisma.prisma_client.modelresponse.create(response_to_save)
    response = requests.post(f"{ML_SERVICE_URL}/v1/process", json={'text': vacancy_ser})

    course = response.json().result
    prisma.prisma_client.modelresponse.update(where={
        "id": response_to_save["id"]
    },
    data = {
        "response": course,
        "finished_at": datetime.datetime.now()
    })

    print(course)
    return f"model call result for vacancy {course[0]}"


def custom_vacancy_decoder(vacancy_dict):
    return namedtuple('X', vacancy_dict.keys())(*vacancy_dict.values())


# Load HTML
def parse_html(html: str) -> str:
    downloaded = trafilatura.fetch_url(html)
    text = trafilatura.extract(downloaded)

    return text
