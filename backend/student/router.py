from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import Response

from database import get_db
from student import models, schemas
from marks import models as mark_models

router = APIRouter()


@router.post("/", response_model=schemas.Student, name='Create a student')
async def create_student(student: schemas.CreateStudent, db: Session = Depends(get_db)):
    if db.query(models.Student).filter_by(name=student.name).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Student already existing')
    student = models.Student(name=student.name)
    db.add(student)
    db.commit()
    db.refresh(student)
    return schemas.Student(student_id=student.student_id, name=student.name, average=0)


@router.get('/', response_model=List[schemas.Student], name='Get all students')
async def get_students(db: Session = Depends(get_db)):
    return sorted([await get_student(i.name, db) for i in db.query(models.Student).all()], key=lambda x: x.average,
                  reverse=True)


@router.get('/{name}', response_model=schemas.Student, name='Get a student by its name')
async def get_student(name: str, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter_by(name=name).first()
    if not student:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    marks = []
    plain_marks = []
    for mark in db.query(mark_models.Mark).filter_by(student=student.student_id).all():
        marks.append({'mark': mark.mark, 'weight': mark.weight})
        [plain_marks.append(mark.mark) for _ in range(mark.weight)]
    average = 0
    try:
        average = round(sum(plain_marks) / len(plain_marks), 2)
    except ZeroDivisionError:
        pass
    student = schemas.Student(student_id=student.student_id, name=student.name, marks=marks, average=average)
    return student


@router.delete('/{name}', name='Delete a student', status_code=status.HTTP_200_OK)
async def delete_student(name: str, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter_by(name=name).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    for mark in db.query(mark_models.Mark).filter_by(student=student.student_id).all():
        db.delete(mark)
    db.delete(student)
    db.commit()
    return Response('Deleted')

