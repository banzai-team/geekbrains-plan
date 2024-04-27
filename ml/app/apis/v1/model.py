from pydantic import BaseModel


class InputCl(BaseModel):
    text: str


class SimularCourse(BaseModel):
    match_score: float
    program_id: int


class OutputCl(BaseModel):
    edu_courses: list[int]
    simular_courses: list[SimularCourse]
