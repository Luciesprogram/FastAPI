from fastapi import FastAPI

app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to Fastapi "}

# about
@app.get("/about")
def about():
    return {"message": "Welcome to Fastapi, this is about "}

# users
@app.get("/users")
def about():
    return {
        "users": ["Mohit","Rohit","Rahul"]
        }

