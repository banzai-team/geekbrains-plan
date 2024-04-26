from typing import Optional
import uvicorn
from pydantic import BaseModel, Field

from app.db import prisma
from fastapi import FastAPI, Response, status
from app.worker import worker

app = FastAPI()


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
def pdf_selection(plan_request: PlanRequest, response: Response):
    if plan_request.url:
        worker.plan_for_url.delay(plan_request.url)
        return {"status": "OK"}
    elif plan_request.text:
        worker.plan_for_text.delay(plan_request.text)
        return {"status": "OK"}

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"status": "ERROR", "message": "url or text must be set"}


@app.post("/api/plan/pdf")
def pdf_selection():
    return True


@app.on_event("startup")
async def startup() -> None:
    await prisma.prisma_client.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await prisma.prisma_client.disconnect()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
