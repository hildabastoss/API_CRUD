from fastapi import HTTPException
from bson import ObjectId
from bson.errors import InvalidId
from models.user import User
from models.todo import ToDo


async def save(obj):
    try:
        find_filter = {'_id': ObjectId(obj.id)}
        to_set = {'$set': obj.dict(by_alias=True, exclude={'id'})}
        await obj.collection().update_one(filter=find_filter, update=to_set, upsert=True)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
async def find_one(id, Model):
    try:
        find_filter = {'_id':ObjectId(id)}
        doc = await Model.collection().find_one(find_filter)
        return Model(**doc)
    except TypeError as e: 
        raise HTTPException(status_code=404, detail='no document found')
    except InvalidId as e:
        raise HTTPException(status_code=400, detail=str(e))
    
async def find_many(Model):
    docs = Model.collection().find()
    return [Model(**doc) async for doc in docs]

async def delete(id, Model):
    try:
        find_filter = {'_id':ObjectId(id)}
        await Model.collection().delete_one(find_filter)
    except Exception as e: 
        pass
    
async def find_todos(user: User):
    print(user)
    docs = ToDo.collection().find({'userId':ObjectId(user.id)})
    # print(docs.count())
    return [ToDo(**doc) async for doc in docs]