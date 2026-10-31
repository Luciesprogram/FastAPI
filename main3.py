#  JSON input handling
# POST request 
# intro to pydantic

from fastapi import FastAPI
from dantic import BaseModel

app = FastAPI()

# @app.post("/create-user")
# def create_user(name:str,age:int):
#     return {
#         "name":name,
#         "age":age
#     }

# @app.post("/create-user")
# def create_user(user:dict):
#     return {
#         "message": "User Created",
#         "Data": user
#     }

# @app.post("/create-user")
# def create_user(user:dict):
#     return {
#         "user name": user['name'],
#         "Age": user['age']
#         }


## Pydantic

class User(BaseModel):
    name: str
    age: int

@app.post("/create-user")
def create_user(user: User):
    return {
        "name": user.name,
        "age": user.age
        }