import uvicorn
from pydantic import BaseModel

from app.db import prisma
from fastapi import FastAPI
from app.worker import worker

app = FastAPI()


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: str = "OK"


class ModelRequest(BaseModel):
    msg: str
    duration: int


@app.get("/ping")
def ping():
    return {"ping": "pong"}


@app.get("/hc")
def healthcheck():
    return HealthCheck(status="OK")


@app.post("/do_work")
def do_work(request: ModelRequest):
    worker.create_task.delay(1, request.duration, request.msg)
    return True


@app.on_event("startup")
async def startup() -> None:
    await prisma.prisma_client.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await prisma.prisma_client.disconnect()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
