import datetime
import logging
import os
import sys
import traceback
from typing import Optional
import uvicorn
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from app.db import prisma
from fastapi import FastAPI, Response, status, UploadFile
from app.worker import worker
import uuid
from strawberry.fastapi import GraphQLRouter
from app.gql import schema

graphql_app = GraphQLRouter(schema.schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
uploads_dir = "/var/planning/uploads"
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HealthCheck(BaseModel):
    status: str = "OK"


class PlanRequest(BaseModel):
    url: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    text: Optional[str] | None = Field(
        default=None, title="The description of the item", max_length=300
    )


@app.get("/hc")
def healthcheck():
    return HealthCheck(status="OK")


@app.post("/api/plan", status_code=201)
def plan_for_text(plan_request: PlanRequest, response: Response):
    request_to_save = {
        "performed_at": datetime.datetime.now(),
        "status": "CREATED"
    }
    request_to_save = prisma.prisma_client.modelrequest.create(request_to_save)
    if plan_request.url:
        async_task = worker.plan_for_url.delay(request_to_save.id, plan_request.url)
        prisma.prisma_client.modelrequest.update(where={"id": request_to_save.id}, data={"task_id": async_task.task_id})
        return {"status": "OK", "taskId": async_task.task_id, "requestId": request_to_save.id}
    elif plan_request.text:
        async_task = worker.plan_for_text.delay(request_to_save.id, plan_request.text)
        prisma.prisma_client.modelrequest.update(where={"id": request_to_save.id}, data={"task_id": async_task.task_id})
        return {"status": "OK", "taskId": async_task.task_id, "requestId": request_to_save.id}

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"status": "ERROR", "message": "url or text must be set"}


@app.post("/api/plan/pdf")
def plan_for_pdf(file: UploadFile, response: Response):
    try:
        if file.content_type != "application/pdf":
            response.status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
            return {"status": "ERROR", "message": "pdf only is supported"}
        request_to_save = {
            "performed_at": datetime.datetime.now()
        }
        request_to_save = prisma.prisma_client.modelrequest.create(request_to_save)
        upload_uuid = uuid.uuid4()
        contents = file.file.read()
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)
        filepath = uploads_dir + "/" + "upload_" + str(upload_uuid) + ".pdf"
        with open(filepath, 'wb') as f:
            f.write(contents)
        async_task = worker.plan_for_pdf.delay(request_to_save.id, filepath)
        prisma.prisma_client.modelrequest.update(where={"id": request_to_save.id}, data={"task_id": async_task.task_id})
        return {"status": "OK", "taskId": async_task.task_id, "requestId": request_to_save.id}
    except Exception as err:
        traceback.print_exception(*sys.exc_info()) 
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": "ERROR", "message": "There was an error uploading the file"}
    finally:
        file.file.close()


@app.on_event("shutdown")
def shutdown() -> None:
    prisma.prisma_client.disconnect()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
