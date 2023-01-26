from models.main_model import MainModel
from db.config import db
from bson import ObjectId
from fastapi import HTTPException


class ToDo(MainModel):
    title: str
    description: str = None
    is_done: bool
    
    async def save(self):
        try:
            find_filter = {'_id': ObjectId(self.id)}
            to_set = {'$set': self.dict(by_alias=True, exclude={'id'})}
            await db.todos.update_one(filter=find_filter, update=to_set, upsert=True)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


# from dataclasses import dataclass

# @dataclass
# class ToDo:
#     title: str
#     description: str
#     is_done: bool

# class ToDo:
#     def __init__(self, title, description, is_done):
#         self.title = title
#         self.description = description
#         self.is_done = is_done
        
#     def __str__(self) -> str:
#         return 'Qualquer coisa'

