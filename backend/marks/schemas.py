from typing import Optional

from pydantic import BaseModel


class Mark(BaseModel):
    class Config:
        orm_mode = True

    mark: int
    weight: int
    student: int


class CreateMark(BaseModel):
    mark: int
    weight: Optional[int]
    student: str
