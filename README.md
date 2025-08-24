### Python FastAPI Crash Course

This is a repository that uses `python3` and `fastAPI` for educational purposes

#### Getting started

- Install python3
- Install fastAPI

```bash
pip3 install fastapi
```

- Install uvicorn

```bash
pip3 install uvicorn
```

#### Running and accessing the server

- To run the server using uvicorn and access the api at `http://localhost:8000/`

```bash
uvicorn api:app --reload
```

#### API

**The Swagger UI is accessible at** `http://localhost:8000/docs`

- GET `/api/`
- GET `/api/students/`
- GET `/api/students/{id}`
- GET `/api/student?name`
- GET `/api/student/{id}?name`
- POST `/api/student/`
