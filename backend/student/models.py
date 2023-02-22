from sqlalchemy import Column, Integer, String

from database import Base


class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(64), unique=True)

    def __repr__(self):
        return self.name
