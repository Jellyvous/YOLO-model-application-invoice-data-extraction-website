# app/database.py
from pymongo import MongoClient
from app.config import Config

# MongoDB connection
client = MongoClient(Config.MONGO_URI)
db = client["yolo"]
users_collection = db["user"]