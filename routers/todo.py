from fastapi import APIRouter
from models.todo import ToDo
from typing import List
from services.todo import find_one_todo, find_todos, delete_todo
from bson import ObjectId

todo_routers = APIRouter()

@todo_routers.get('/', response_model=List[ToDo])
async def to_do_list():
    """
    List all to do in database
    """
    return await find_todos()
    
@todo_routers.get('/{id}', response_model=ToDo)
async def to_do(id):
    return await find_one_todo(id=id)

@todo_routers.post('/', status_code=201)
async def create_to_do(todo: ToDo):
    await todo.save()
    # return await create_todo(todo=todo)

@todo_routers.put('/{id}')
async def update_to_do(id, todo: ToDo):
    todo.id = ObjectId(id)
    await todo.save()
    # return await update_todo(id=id, todo=todo)

@todo_routers.delete('/{id}')
async def delete_to_do(id):
    return await delete_todo(id=id)