from pydantic import BaseModel, Field, validator


def to_camel_case(value:str):
    words = value.split('_')
    result = words[0]
    for word in words[1:]:
        result += word.title()
    return result

class MainModel(BaseModel):
    id: str = Field(alias='_id', default=None)
    
    @validator('id', pre=True)
    def oid_converter(cls, value):
        try:
            return str(value)
        except TypeError:
            return value

    class Config:
        alias_generator = to_camel_case