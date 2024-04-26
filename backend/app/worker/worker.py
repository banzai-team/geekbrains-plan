import datetime
import os
import time

from celery import Celery
from app.db import prisma


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="create_task")
def create_task(request_id, task_time, msg):
    time.sleep(int(task_time) * 10)
    prisma.prisma_client.modelresponse.create({
        "request_id": request_id,
        "started_at": datetime.datetime.now()
    })
    return True
