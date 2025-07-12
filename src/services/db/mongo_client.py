from motor.motor_asyncio import AsyncIOMotorClient
from src.config.settings import settings

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]