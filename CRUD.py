"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id : int
    title: str
    completed: bool

@app.post("/add-todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {
        "message": "Todo added successfully",
        "Todo": todo.title
    }


@app.get("/fetch-all")
def get_todo():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"erro": "Todo not found"}
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

@app.post("/add-todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {
        "message":"Todo added succesfully",
        "title": todo.title
    }

@app.get("/fetch-all")
def get_all_todo():
    return todos

@app.get("/get-todo/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {
                "title": todo.title,
                "completed": todo.completed
            }
    return {"error": "No record found"}


@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, updated_todo: Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {
                "message": "Data Updated succesfully",
                "data": updated_todo
            }
    return {"error": "No record found"}
