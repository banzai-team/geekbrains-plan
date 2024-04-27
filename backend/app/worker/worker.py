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
def plan_for_text(request_id, text: str):
    return chain(text_extraction.s(request_id, text), model_invocation.s()).delay()


@celery.task(name="create_url_workflow")
def plan_for_url(request_id,url: str):
    return chain(url_extraction.s(request_id, url), model_invocation.s()).delay()


@celery.task(name="create_pdf_workflow")
def plan_for_pdf(request_id, text: str):
    return chain(pdf_extraction.s(request_id, text), model_invocation.s()).delay()


@celery.task(name="pdf_extraction")
def pdf_extraction(request_id, file_path: str) -> str:
    prisma.prisma_client.modelrequest.update(where={"id": request_id}, data={
        "source": file_path,
        "source_type": "pdf",
        "status": "PARSING"
    })
    try:
        pdf_loader = PyPDFLoader(file_path)
        pages = pdf_loader.load()
        text = ""
        for page in pages:
            text += page.page_content

        prisma.prisma_client.modelrequest.update(where={"id": request_id}, data={
            "extracted_text": text,
        })

        logger.debug(f"extracted text from {file_path}: {text}")

        return json.dumps({
            "request_id": request_id,
            "text": text
        })
    except Exception as err:
        prisma.prisma_client.modelrequest.update(where={"id": request_id}, data={
            "status": f"ERROR. Reason:{err}"
        })
        raise err
    


@celery.task(name="url_extraction")
def url_extraction(request_id, url: str):
    prisma.prisma_client.modelrequest.update(where={"id": request_id}, data={
        "source": url,
        "source_type": "url",
        "status": "PARSING"
    })

    try:
        extracted_text = parse_html(url)

        prisma.prisma_client.modelrequest.update(where={"id": request_id}, data={
            "extracted_text": extracted_text,
        })
        return json.dumps({
            "request_id": request_id,
            "text": extracted_text
        })
    except Exception as err:
        prisma.prisma_client.modelrequest.update(where={"id": request_id}, data={
            "status": f"ERROR. Reason:{err}"
        })
        raise err
    


@celery.task(name="text_extraction")
def text_extraction(request_id, text: str) -> str:
    prisma.prisma_client.modelrequest.update(where={"id": request_id}, data={
        "source": text,
        "source_type": "text",
        "status": "PARSING"
    })

    return json.dumps({
        "request_id": request_id,
        "text": text
    })


@celery.task(name="model_invocation")
def model_invocation(ser: str) -> str:
    try:
        des = json.loads(ser)
        prisma.prisma_client.modelrequest.update(where={"id": des["request_id"]}, data={
            "req_text": des["text"],
            "status": "ANALYZING"
        })
        response_to_save = {
            "request_id": des["request_id"],
            "started_at": datetime.datetime.now()
        }
        response_to_save = prisma.prisma_client.modelresponse.create(response_to_save)
        response = requests.post(f"{ML_SERVICE_URL}/v1/process", json={'text': des["text"]})

        course = response.json()
        edu_courses = course["edu_courses"]
        simular_courses = course["simular_courses"]

        print(course)
        # course = json.dumps({"data": [0,1,2]})
        prisma.prisma_client.modelresponse.update(where={
            "id": response_to_save.id
        },
        data = {
            "finished_at": datetime.datetime.now(),
            "course_coverage": course["course_coverage"] if "course_coverage" in course else None,
            "meta": json.dumps({
                "skills_need": course["skills_need"] if "course_coverage" in course else []
            })
        })

        for course in edu_courses:
            course = prisma.prisma_client.outputcleducourse.create({
                "program": {
                    "connect": {
                        "id": int(course)
                    }
                },
                "response": {
                    "connect": {
                        "id": int(response_to_save.id)
                    }
                }
            })

        for simular_course in simular_courses:
            course = prisma.prisma_client.outputclsimularcourse.create({
                "match_score": simular_course["match_score"],
                "program": {
                    "connect": {
                        "id": int(simular_course["program_id"])
                    }
                },
                "response": {
                    "connect": {
                        "id": int(response_to_save.id)
                    }
                }
            })

        prisma.prisma_client.modelrequest.update(where={"id": des["request_id"]}, data={
            "status": "PROCESSED"
        })

        return f"model call result for vacancy {course}"
    except Exception as err:
        prisma.prisma_client.modelrequest.update(where={"id": des["request_id"]}, data={
            "status": f"ERROR. Reason:{err}"
        })
        raise err
    


def custom_vacancy_decoder(vacancy_dict):
    return namedtuple('X', vacancy_dict.keys())(*vacancy_dict.values())


# Load HTML
def parse_html(html: str) -> str:
    downloaded = trafilatura.fetch_url(html)
    text = trafilatura.extract(downloaded)

    return text
