from fastapi import FastAPI
from db.config import db
from models.todo import ToDo

app = FastAPI(
    title='To Do API', 
    description='This is a To do API for dummies',
    version='0.1'
)

@app.get('/todo')
def to_do_list():
    """
    List all to do in database
    """
    docs = db.todos.find()
    return [ToDo(**doc) for doc in docs]
