from models.main_model import MainModel, ObjId
from db.config import db



class ToDo(MainModel):
    user_id: ObjId = None
    title: str
    description: str = None
    is_done: bool
    
    @classmethod
    def collection(cls):
        return db.todos
    