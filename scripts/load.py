import pandas as pd
from pymongo import MongoClient
from config.mongo_config import MONGO_URI, DATABASE_NAME, COLLECTION_NAME

def load_data():
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    df = pd.read_csv("../data/processed/transformed_data.csv")
    data = df.to_dict(orient='records')
    collection.insert_many(data)
    return data
