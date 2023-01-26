from fastapi import APIRouter
from routers.todo import todo_routers
from routers.users import user_routers

app_routers = APIRouter()

app_routers.include_router(router=todo_routers, prefix='/todo')
app_routers.include_router(router=user_routers, prefix='/user')