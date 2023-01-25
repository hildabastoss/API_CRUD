from fastapi import FastAPI
from routers.app_routers import app_routers

app = FastAPI(
    title='To Do API', 
    description='This is a To do API for dummies',
    version='0.1'
)
app.include_router(router=app_routers)
    
