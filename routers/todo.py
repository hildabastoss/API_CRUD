from fastapi import APIRouter, HTTPException, status
from db.config import db
from models.todo import ToDo
from typing import List
from bson import ObjectId
from bson.errors import InvalidId


todo_routers = APIRouter()

@todo_routers.get('/', response_model=List[ToDo])
async def to_do_list():
    """
    List all to do in database
    """
    docs = db.todos.find()
    return [ToDo(**doc) async for doc in docs]

@todo_routers.get('/{id}')
async def to_do(id):
    try:
        find_filter = {'_id':ObjectId(id)}
        doc = await db.todos.find_one(find_filter)
        return ToDo(**doc)
    except TypeError as e: 
        raise HTTPException(status_code=404, detail='no document found')
    except InvalidId as e:
        raise HTTPException(status_code=400, detail=str(e))