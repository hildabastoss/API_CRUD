from pydantic import BaseModel, Field, validator
from bson import ObjectId

def to_camel_case(value:str):
    words = value.split('_')
    result = words[0]
    for word in words[1:]:
        result += word.title()
    return result

class MainModel(BaseModel):
    id: str = Field(alias='_id', default=None)
    
    @validator('id', pre=True)
    def oid_converter(cls, value: ObjectId):
        return str(value)
        
    class Config:
        alias_generator = to_camel_case