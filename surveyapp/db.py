from pymongo import MongoClient

MONGO_URI = "mongodb+srv://mongouser:mongoisbest@cluster0.9nbsswg.mongodb.net/?retryWrites=true&w=majority"

# For JD Database
def db_name():
    client = MongoClient(MONGO_URI)
    db = client["adaniAirport"]
    
    return db