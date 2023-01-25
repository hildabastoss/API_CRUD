from models.todo import ToDo
from fastapi import HTTPException
from bson import ObjectId
from bson.errors import InvalidId
from db.config import db

async def find_todos():
    docs = db.todos.find()
    return [ToDo(**doc) async for doc in docs]

async def find_one_todo(id):
    try:
        find_filter = {'_id':ObjectId(id)}
        doc = await db.todos.find_one(find_filter)
        return ToDo(**doc)
    except TypeError as e: 
        raise HTTPException(status_code=404, detail='no document found')
    except InvalidId as e:
        raise HTTPException(status_code=400, detail=str(e))
    
async def create_todo(todo: ToDo):
    doc = todo.dict(by_alias=True, exclude={'id'})
    try:
        await db.todos.insert_one(doc)
    except Exception:
        raise HTTPException(status_code=400)
    
async def update_todo(id, todo: ToDo):
    try:
        find_filter = {'_id':ObjectId(id)}
        to_set = {'$set': todo.dict(by_alias=True, exclude={'id'})}
        await db.todos.update_one(find_filter, to_set)
    except TypeError as e: 
        raise HTTPException(status_code=404, detail='no document found')
    except InvalidId as e:
        raise HTTPException(status_code=400, detail=str(e))
    
async def delete_todo(id):
    try:
        find_filter = {'_id':ObjectId(id)}
        await db.todos.delete_one(find_filter)
    except Exception as e: 
        pass
    

    