from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

class Employee(BaseModel):
    id: int
    name: str
    email: str
    dept: str
    
@app.get("/")
def get_home_page():
    return {"message": "Welcome to the Employee Management System"}

#print(get_home_page())

if __name__ == '__main__':
    run("main:app",host="0.0.0.0",port=8000,reload=True)