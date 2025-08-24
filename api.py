from fastapi import FastAPI, Path

app = FastAPI()

students = [{
    "id": 1,
    "name": "Nick",
    "age": 17,
    "class": "A1"
}]

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