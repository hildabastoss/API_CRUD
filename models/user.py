from models.main_model import MainModel
from db.config import db
from pydantic import validator


class User(MainModel):
    username: str
    password: str
    

    @classmethod
    def collection(cls):
        return db.users
    