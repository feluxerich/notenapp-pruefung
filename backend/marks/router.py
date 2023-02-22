from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from marks import schemas, models
from student.router import get_student

router = APIRouter()


@router.post('/', response_model=schemas.Mark, name='Create a mark for a student')
async def create_mark(mark: schemas.CreateMark, db: Session = Depends(get_db)):
    weight: int = mark.weight
    student = await get_student(mark.student, db)
    student_id = student.student_id
    if weight == 0 or weight is None:
        weight = 1
    mark = models.Mark(student=student_id, mark=mark.mark, weight=weight)
    db.add(mark)
    db.commit()
    db.refresh(mark)
    return mark
