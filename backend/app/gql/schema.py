import datetime
from datetime import date
from random import randint
from typing import Optional, List

import strawberry
from app.db import prisma


@strawberry.type
class ModelResponse:
    id: int
    response: Optional[str]
    started_at: Optional[date]
    finished_at: Optional[date]


@strawberry.type
class ModelRequest:
    id: int
    request: Optional[str] = None
    performed_at: Optional[date] = None
    response: Optional[ModelResponse]


@strawberry.type
class Module:
    id: int
    title: str


@strawberry.type
class Quarter:
    id: int
    title: str

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
    modules: Optional[Module]
    quarter: Optional[Quarter]




@strawberry.type
class Query:
    @strawberry.field()
    def model_requests(self) -> List[ModelRequest]:
        return prisma.prisma_client.modelrequest.find_many(include={
            "response": True
        })

    @strawberry.field()
    def model_request(self, id: int) -> ModelRequest:
        return prisma.prisma_client.modelrequest.find_unique(where={"id": id}, include={
            "response": True
        })
    
    @strawberry.field()
    def programs(self) -> List[Program]:
        return prisma.prisma_client.program.find_many(include={
            "modules": True,
            "quarters": True,
        })
    
    @strawberry.field()
    def program(self, id: int) -> Program:
        return prisma.prisma_client.program.find_unique(where={"id": id}, include={
            "modules": True,
            "quarters": True,
        })
    

schema = strawberry.Schema(query=Query)
