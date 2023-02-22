from sqlalchemy import Column, Integer, ForeignKey

from database import Base


class Mark(Base):
    __tablename__ = 'marks'

    mark_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    mark = Column(Integer)
    weight = Column(Integer)
    student = Column(ForeignKey("students.student_id"))
