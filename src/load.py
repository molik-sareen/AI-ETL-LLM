import pymysql
import pymongo
import pandas as pd
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

def load_to_mysql(df, table_name):
    df.to_sql(table_name, MYSQL_CONN, if_exists="replace", index=False)

def load_to_mongo(df, collection_name):
    collection = MONGO_DB[collection_name]
    collection.insert_many(df.to_dict(orient="records"))

