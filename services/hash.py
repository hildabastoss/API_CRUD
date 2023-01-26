from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='user/login')

pwd_context = CryptContext(schemes=['bcrypt'])
secret_key = '150E9DE319EB46AB4DBC48D7346579BBFF6A6159DC9722CC839F4373B54B3F50'
algorithm = 'HS256'
token_expire_minutes = 3600

def generate_pwd_hash(value: str):
    return pwd_context.hash(secret=value)

def generate_hash(data: dict):
    expire_date = datetime.utcnow() + timedelta(minutes=token_expire_minutes)
    data = {'sub':data, 'exp':expire_date}
    return jwt.encode(claims=data, key=secret_key, algorithm=algorithm)

def get_data_from_hash(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token=token, key=secret_key, algorithms=[algorithm])
    return payload.get('sub')
    
