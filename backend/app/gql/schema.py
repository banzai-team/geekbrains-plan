import datetime
from datetime import date
from random import randint
from typing import Optional, List

import strawberry
from app.db import prisma


@strawberry.type
class ModelRequest:
    id: int
    request: Optional[str] = None
    requested_at: Optional[date] = None
    started_at: Optional[date] = None
    finished_at: Optional[date] = None


@strawberry.type
class Program:
    id: int
    name: str
    speciality: Optional[str]
    url: Optional[str]
    tag: Optional[str]
    difficulty: Optional[str]
    price: Optional[int]
    days_amount: Optional[int]


@strawberry.type
class Query:
    @strawberry.field()
    async def model_requests(self) -> List[ModelRequest]:
        return await prisma.prisma_client.modelrequest.find_many()

    @strawberry.field()
    async def model_request(self, id: int) -> ModelRequest:
        return await prisma.prisma_client.modelrequest.find_unique(where={"id": id})
    

schema = strawberry.Schema(query=Query)
