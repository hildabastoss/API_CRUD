# from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

uri = 'mongodb://localhost:27017'

client = MongoClient(uri)

# client = AsyncIOMotorClient(uri)
db = client.First_DB