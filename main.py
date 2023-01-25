from fastapi import FastAPI, HTTPException, status
from db.config import db
from models.todo import ToDo
from typing import List
from bson import ObjectId
from bson.errors import InvalidId


app = FastAPI(
    title='To Do API', 
    description='This is a To do API for dummies',
    version='0.1'
)

@app.get('/todo', response_model=List[ToDo])
def to_do_list():
    """
    List all to do in database
    """
    docs = db.todos.find()
    return [ToDo(**doc) for doc in docs]

@app.get('/todo/{id}')
def to_do(id):
    try:
        find_filter = {'_id':ObjectId(id)}
        doc = db.todos.find_one(find_filter)
        return ToDo(**doc)
    except TypeError as e: 
        raise HTTPException(status_code=404, detail='no document found')
    except InvalidId as e:
        raise HTTPException(status_code=400, detail=str(e))
    
