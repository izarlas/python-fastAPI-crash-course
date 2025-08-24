from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    age: int

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None

students: list[Student] = [
    Student(
        id = 1,
        name = "Nick",
        age = 17,
    )
]

@app.get('/api/')
def index():
    return {"name": "/api"}

@app.get('/api/students/', response_model=list[Student])
def find_students():
    return students

@app.get('/api/student/{id}', response_model=Student)
def find_student_by_id(id: int = Path(..., description="The student id", gt=0)):
    return next((student for student in students if student.id == id), None)

@app.get('/api/student', response_model=Student)
def find_student_by_name(name: str):
    for student in students:
        if student.name == name:
            return student

    raise HTTPException(status_code = 404, detail = "Student not found")

@app.get('/api/student/{id}', response_model=Student)
def find_student_by_id_and_name(id: int, name: str):
    for student in students:
        if student.id == id and student.name == name:
            return student

    raise HTTPException(status_code = 404, detail = "Student not found")

@app.post('/api/student/', response_model=list[Student])
def create_student(student: Student):
    if student.id in students:
        raise HTTPException(status_code=409, detail="Student already exists")

    students.append(student)
    return students

@app.put('/api/student/{id}', response_model=list[Student])
def update_student_by_id(id: int, update_student: UpdateStudent):
    student_to_update = next((student for student in students if student.id == id), None)

    if student_to_update is None:
        raise HTTPException(status_code = 404, detail = "Student not found")

    if update_student.name is not None:
        student_to_update.name = update_student.name
    if update_student.age is not None:
        student_to_update.age = update_student.age
        
    return students

@app.delete('/api/student/{id}', response_model=list[Student])
def delete_student_by_id(id: int):
    student = next((student for student in students if student.id == id), None)

    if student is None:
        raise HTTPException(status_code = 404, detail = "Student not found")

    students.remove(student)
    return students