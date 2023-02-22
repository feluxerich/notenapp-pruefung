from typing import List

from pydantic import BaseModel


class Student(BaseModel):
    class Config:
        orm_mode = True

    student_id: int
    name: str
    marks: List[dict] = []
    average: float


class CreateStudent(BaseModel):
    name: str


class UpdateStudent(BaseModel):
    name: str
