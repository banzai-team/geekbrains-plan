from pydantic import BaseModel

class InputCl(BaseModel):
    text: str

class OutputCl(BaseModel):
    result: list[int]
