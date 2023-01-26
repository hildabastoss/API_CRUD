from fastapi import APIRouter, Depends
from models.todo import ToDo
from typing import List
from bson import ObjectId
from services.db import save, find_one, delete, find_todos
from services.user import get_current_user
from models.user import User

todo_routers = APIRouter()

@todo_routers.get('/', response_model=List[ToDo])
async def to_do_list(user: User = Depends(get_current_user)):
    """
    List all to do in database
    """
    return await find_todos(user=user)
    
@todo_routers.get('/{id}', response_model=ToDo)
async def to_do(id):
    return await find_one(id=id, Model=ToDo)

@todo_routers.post('/', status_code=201)
async def create_to_do(todo: ToDo, user: User = Depends(get_current_user)):
    todo.user_id = user.id
    await save(todo)

@todo_routers.put('/{id}')
async def update_to_do(id, todo: ToDo):
    todo.id = ObjectId(id)
    await save(todo)

@todo_routers.delete('/{id}')
async def delete_to_do(id):
    return await delete(id=id, Model=ToDo)