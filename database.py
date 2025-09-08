from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(mongo_uri)
db = client[os.getenv("DATABASE_NAME")]



# Collections
users_collection = db["users"]
products_collection = db["products"]
orders_collection = db["orders"]
order_items_collection = db["order_items"]