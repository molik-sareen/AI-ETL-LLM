import pymysql
import pymongo
import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# MySQL Connection
MYSQL_CONN = pymysql.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASS"),
    database=os.getenv("MYSQL_DB")
)

# MongoDB Connection
MONGO_CLIENT = pymongo.MongoClient(os.getenv("MONGO_URI"))
MONGO_DB = MONGO_CLIENT[os.getenv("MONGO_DB")]

def extract_mysql(table_name):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, MYSQL_CONN)
    return df

def extract_mongo(collection_name):
    collection = MONGO_DB[collection_name]
    data = list(collection.find())
    return pd.DataFrame(data)

def extract_api(url):
    response = requests.get(url)
    return pd.DataFrame(response.json())

