from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class User(BaseModel):
#     name: str
#     age: int
#     email: str

# @app.post("/create-user")
# def user_create(user: User):
#     return {
#         "massage": "User created",
#         "name": user.name,
#         "age": user.age
#     }

## Nested Model

class Address(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    name: str
    age: int
    address: Address

@ app.post("/create-user")
def create_user(user:User):
    return {
        "message": "User Created",
        "Name": user.name,
        "Age": user.age,
        "City": user.address.city,
        "Pincode": user.address.pincode      

    }
