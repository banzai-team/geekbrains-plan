import uvicorn
from app.db import prisma
from fastapi import FastAPI

app = FastAPI()
app.include_router(graphql_app, prefix="/gql")

@app.get("/")
def ping():
    return {"ping": "pong"}


@app.on_event("startup")
async def startup() -> None:
    await prisma.prisma_client.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await prisma.prisma_client.disconnect()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
