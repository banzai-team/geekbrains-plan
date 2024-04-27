import json
import os
from collections import namedtuple

import requests
from bs4 import BeautifulSoup
from celery import Celery
from celery import chain
from langchain_community.document_loaders import AsyncChromiumLoader

from app.config.config import ML_SERVICE_URL

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


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
    response = requests.post(ML_SERVICE_URL, json={'text': vacancy_ser})

    course = response.json().result
    print(course)
    return f"model call result for vacancy {course[0]}"


def custom_vacancy_decoder(vacancy_dict):
    return namedtuple('X', vacancy_dict.keys())(*vacancy_dict.values())


# Load HTML
def parse_html(html: str) -> str:
    loader = AsyncChromiumLoader([html])
    html = loader.load()

    soup = BeautifulSoup(html[0].page_content, 'html.parser')

    # Remove all tags except 'text' and 'div'
    for tag in soup.find_all(True):
        if tag.name not in ['p', 'ul', 'li', 'div'] + [f"h{i}" for i in range(1, 6)]:
            tag.unwrap()

    for tag in soup.find_all(True):
        tag.attrs = {}
        if not tag.get_text(strip=True):
            tag.decompose()

    sample_text = str(soup)
    sample_text = '\n'.join(line.strip() for line in sample_text.split('\n') if len(line.strip()) > 0)

    return sample_text
