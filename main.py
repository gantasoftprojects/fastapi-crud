from http.client import HTTPException

from fastapi import FastAPI
from fastapi.params import Depends

from database import get_db
from model import Student
from schema import StudentRequest

app = FastAPI()

@app.get("/students")
async def get_students(db=Depends(get_db)):
    return  db.query(Student).all()

@app.get("/students/{id}")
async def get_student(id: int, db=Depends(get_db)):
    return db.query(Student).get(id)

@app.post("/student")
async def create_student(student: StudentRequest, db=Depends(get_db)):
    new_student = Student(id=student.id, name=student.name, mobile=student.mobile)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.put("/student/{id}")
def update_student(id:int,student: StudentRequest, db=Depends(get_db)):
  #step1: find the existing student
   db_student=db.query(Student).filter(Student.id == id).first()
  #sep2:    check student exist or not
   if not db_student:
         raise HTTPException(status_code=404, detail="Student not found")
#   step3: update values
   db_student.name = student.name
   db_student.mobile = student.mobile
#    step4: save changes
   db.commit()
#   step5: refresh updated data
   db.refresh(db_student)
   return db_student
@app.delete("/student/{id}")
def delete_student(id:int, db=Depends(get_db)):
    # step1: find the existing student
    db_student = db.query(Student).filter(Student.id == id).first()
    # sep2:    check student exist or not
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
#   step3: update values
    db.delete(db_student)
    db.commit()
    return {"message": "Student deleted"}