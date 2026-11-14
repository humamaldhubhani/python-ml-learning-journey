from fastapi import FastAPI
from enum import Enum

app = FastAPI()
class available (str,Enum):
    names = "names"
    ages = "ages"
    id = "id"

student = {
    "names" : ["Humam","Ahmed","Eyad"],
    "ages" : ["21","21","21"],
    "id" : [1,2,3],

}

@app.get("/get/{info}")
async def hello(info:available):
    return student.get(info)