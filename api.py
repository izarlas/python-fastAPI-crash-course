from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

students = [{
    "id": 1,
    "name": "Nick",
    "age": 17,
}]

class Student(BaseModel):
    id: int
    name: str
    age: int

@app.get('/api/')
def index():
    return {"name": "/api"}

@app.get('/api/students/')
def find_students():
    return students

@app.get('/api/students/{id}')
def find_student_by_id(id: int = Path(..., description="The student id", gt=0)):
    return next((student for student in students if student["id"] == id), None)

@app.get('/api/student')
def find_student_by_name(name: str):
    for student in students:
        if student["name"] == name:
            return student

    return {"Error": "Student not found"}

@app.get('/api/student/{id}')
def find_student_by_id_and_name(id: int, name: str):
    for student in students:
        if student["id"] == id and student["name"] == name:
            return student

    return {"Error": "Student not found"}

@app.post('/api/student/')
def create_student(student: Student):
    if (student.id in students):
        return {"Error": "Student already exists"}

    students.append(student)
    return students