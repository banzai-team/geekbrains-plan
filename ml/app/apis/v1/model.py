from pydantic import BaseModel, Field


class InputCl(BaseModel):
    text: str


class SimularCourse(BaseModel):
    match_score: float = Field(..., description="simular score")
    program_id: int


class SkillsNeeded(BaseModel):
    skill_name: str
    requirement: int = Field(
        ..., description="\"-1\" - навык не требуется; \"0\" - навык будет полезен; \"1\" - навык необходим."
    )


class OutputCl(BaseModel):
    edu_courses: list[int]
    simular_courses: list[SimularCourse]
    skills_need: list[SkillsNeeded]
    course_coverage: float = Field(..., description="Можно ли сразу после курса приступать к работе по профессии в вакансии? От 0 до 1")
