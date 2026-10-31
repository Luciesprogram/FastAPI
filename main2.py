# dynamic routes
# data types
# validation basics

from fastapi import FastAPI

app = FastAPI()

# # about
# @app.get("/users/{user_id}")
# def get_users(user_id:int):
#     return {"user id":user_id}


# Query parameters

# @app.get("/users")
# def get_users(name):
#     return {"name":name}

# optional parameter

@app.get("/users")
def get_users(name: str = None):
    return {"name":name}

@app.get("/products")
def get_products(limit: int = 10):
    return {"limit": limit}

@app.get("/items")
def get_items(name: str=None, price: int = 0):
    return {
        "Name": name,
        "Price": price
    }