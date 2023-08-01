from pymongo import MongoClient

import os
from dotenv import load_dotenv
load_dotenv()

MONGO_URI = "mongodb+srv://mongouser:mongoisbest@cluster0.9nbsswg.mongodb.net/?retryWrites=true&w=majority"

# For JD Database
def db_name():
    client = MongoClient(MONGO_URI)
    db = client["adaniAirport"]
    
    return db