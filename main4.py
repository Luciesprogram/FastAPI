# Path + Query + Body combo 

from re import I

from fastapi import FastAPI
from huggingface_hub import ModelCard
from psutil import users
from pydantic import BaseModel
from sklearn.model_selection import ValidationCurveDisplay

app = FastAPI()

# PUT /users/101?nitify=True
# {
#     "name": "Mohit",
#     "age": 24
# }

# users = []

# class User(BaseModel):
#     name: str
#     age: int

# @app.post("/users")
# def create_user(user:User):
#     users.append(user)  
#     return{
#         "message": "User Created",
#         "data": user
#     }

# @app.put("/users/{user_id}")
# def updated_user(user_id:int, user:User, notify:bool = False):
#     if user_id < len(users):
#         users[user_id] = user
#         return {
#             "message": "User Updated",
#             "notify": notify,
#             "data": user
#         }
#     return {
#         "error": "User not found"
#     }

# video - 10

# Response Model = woh data ham client to deta hai means 
# hame jo data hide karni ho uuse hide karthe hai or jo user specific ho sirf wahi show karthe hai unhe
# 1. Response Validation
# 2. Hide Sensitive Data
# 3. Output formatting

class User(BaseModel):
    name: str
    age: int
    password: str

class UserResponse(BaseModel):
    name: str
    age: int


@app.get("/user",response_model=UserResponse)
def get_user():
    return {
        "name": "Mohit",
        "age": 22,
        "password": "12345"
    }

# Request model = getting data from client (input define), isme input data ko define and validate karthe hai jo frontend se aa rha ho.
# Respone model = geving response to client (output define), isme output data define or valiadate karthe hai jo frontend ko bhejthe hai.