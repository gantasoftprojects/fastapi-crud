from pydantic import BaseModel

# {"id":3,"name":"Suresh","mobile":"789887777"}
class StudentRequest(BaseModel):
    id: int
    name: str
    mobile: str