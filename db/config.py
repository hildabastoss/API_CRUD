from motor.motor_asyncio import AsyncIOMotorClient

uri = 'mongodb://localhost:27017'

client = AsyncIOMotorClient(uri)
db = client.First_DB