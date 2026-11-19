from fastapi import FastAPI
from fastapi.params import Depends

from database import get_db
from model import Student

app = FastAPI()

@app.get("/students")
async def get_students(db=Depends(get_db)):
    return  db.query(Student).all()

@app.get("/students/{id}")
async def get_student(id: int, db=Depends(get_db)):
    return db.query(Student).get(id)