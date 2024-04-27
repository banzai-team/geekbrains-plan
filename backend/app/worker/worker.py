import json
import logging
import os
from collections import namedtuple

import requests
from bs4 import BeautifulSoup
from celery import Celery
from celery import chain
from langchain_community.document_loaders import AsyncHtmlLoader, AsyncChromiumLoader
from langchain_community.document_loaders import PyPDFLoader
import trafilatura

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from app.config.config import ML_SERVICE_URL

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
    response = requests.post(f"{ML_SERVICE_URL}/v1/process", json={'text': vacancy_ser})

    courses = response.json()["edu_courses"]
    similar_courses = response.json()["simular_courses"]
    print(courses)
    return f"model call result for vacancy {courses[0]}"


def custom_vacancy_decoder(vacancy_dict):
    return namedtuple('X', vacancy_dict.keys())(*vacancy_dict.values())


# Load HTML
def parse_html(html: str) -> str:
    downloaded = trafilatura.fetch_url(html)
    text = trafilatura.extract(downloaded)

    return text
    # loader = AsyncHtmlLoader([html])
    # loader = AsyncChromiumLoader([html])
    # html = loader.load()

    soup = BeautifulSoup(html[0].page_content, 'html.parser')

    # Remove all tags except 'text' and 'div'
    for tag in soup.find_all(True):
        if tag.name not in ['p', 'ul', 'li', 'div'] + [f"h{i}" for i in range(1, 6)]:
            tag.unwrap()

    for tag in soup.find_all(True):
        tag.attrs = {}
        if not tag.get_text(strip=True):
            tag.decompose()

    sample_text = str(soup.text)
    sample_text = '\n'.join(line.strip() for line in sample_text.split('\n') if len(line.strip()) > 0)

    return sample_text
