from models.main_model import MainModel
from db.config import db


class ToDo(MainModel):
    title: str
    description: str = None
    is_done: bool
    
    @classmethod
    def collection(cls):
        return db.todos
    