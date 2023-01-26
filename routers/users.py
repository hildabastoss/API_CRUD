from fastapi import APIRouter, HTTPException, Depends
from typing import List
from models.users import User
from bson import ObjectId
from services.db import save, find_one, find_many, delete
from services.hash import generate_pwd_hash
from services.user import is_user_in_db, get_token
from fastapi.security import OAuth2PasswordRequestForm


user_routers = APIRouter()

@user_routers.get('/', response_model=List[User])
async def users_list():
    """
    List all users in database
    """
    return await find_many(Model=User)

@user_routers.get('/{id}', response_model=User)
async def users(id):
    return await find_one(id=id, Model=User)

@user_routers.post('/', status_code=201)
async def create_users(user: User):
    if await is_user_in_db(username=user.username):
        raise HTTPException(status_code=400, detail='Try another username')
    user.password = generate_pwd_hash(user.password)
    await save(user)
    
@user_routers.put('/{id}')
async def update_users(id, user: User):
    user.id = ObjectId(id)
    await save(user)

@user_routers.delete('/{id}')
async def delete_user(id):
    return await delete(id=id, Model=User)

@user_routers.post('/login')
async def token(form:OAuth2PasswordRequestForm = Depends()):
    user = User(username=form.username, password=form.password)
    return await get_token(user=user)
    
    
    