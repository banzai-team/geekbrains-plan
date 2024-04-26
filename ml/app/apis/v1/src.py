from fastapi import status
from fastapi.routing import APIRouter

from .model import InputCl, OutputCl

router = APIRouter(prefix="/v1")


@router.post('/process',
             description='Тест',
             tags=['Inference endpoints'],
             status_code=status.HTTP_200_OK,
             response_model=OutputCl)
def sum_(input_: InputCl) -> OutputCl:
    return OutputCl(result=[])
