from fastapi import APIRouter
from routers.todo import todo_routers

app_routers = APIRouter()

app_routers.include_router(router=todo_routers, prefix='/todo')