from fastapi import status
from fastapi.routing import APIRouter

from .model import InputCl, OutputCl
from app.core.llm import narrow

router = APIRouter(prefix="/v1")


@router.post('/process',
             description='Тест',
             tags=['Inference endpoints'],
             status_code=status.HTTP_200_OK,
             response_model=OutputCl)
def sum_(input_: InputCl) -> OutputCl:
    llm_result = narrow(header="", sample_text=input_.text)
    return OutputCl(result=llm_result)
