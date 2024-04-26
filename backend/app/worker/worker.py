import datetime
import os
import time

from celery import Celery
import json
from celery import chain, group, chord
from collections import namedtuple


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="create_html_workflow")
def plan_for_url(url: str):
    chain(url_extraction.s(url), model_invocation.s()).delay()
    return True


@celery.task(name="create_html_workflow")
def plan_for_url(url: str):
    chain(url_extraction.s(url), model_invocation.s()).delay()
    return True


@celery.task(name="create_pdf_workflow")
def plan_for_text(text: str):
    chain(text_extraction.s(text), model_invocation.s()).delay()
    return True


@celery.task(name="pdf_extraction")
def pdf_extraction(file_path: str) -> str:
    return json.dumps({
        "title": f"some_vacancy_from_pdf: {file_path}"
    })


@celery.task(name="url_extraction")
def url_extraction(url: str) -> str:
    return json.dumps({
        "title": f"some_vacancy_from_url: {url}"
    })


@celery.task(name="text_extraction")
def text_extraction(text: str) -> str:
    return json.dumps({
        "title": f"some_vacancy_from_text: {text}"
    })


@celery.task(name="model_invocation")
def model_invocation(vacancy_ser: str) -> str:
    vacancy = json.loads(vacancy_ser, object_hook=custom_vacancy_decoder)
    return f"model call result for vacancy {vacancy.title}"


def custom_vacancy_decoder(vacancy_dict):
    return namedtuple('X', vacancy_dict.keys())(*vacancy_dict.values())

