from services.hash import pwd_context, generate_hash, get_data_from_hash
from models.user import User
from fastapi import HTTPException, Depends


async def is_user_in_db(username: str):
    doc = await User.collection().find_one({'username':username})
    if doc:
        return True
    return False


async def get_token(user:User):
    error = HTTPException(status_code=404, detail='incorrect username or password')

    doc = await User.collection().find_one({'username':user.username})
    if not doc:
        raise error
    user_db = User(**doc)
    if not pwd_context.verify(secret=user.password, hash=user_db.password):
        raise error
    access_token = generate_hash(user_db.username)
    return {'access_token':access_token, 'token_type':'baerer'}

async def get_current_user(username: str = Depends(get_data_from_hash)):
    doc = await User.collection().find_one({'username':username})
    return User(**doc)

    