from pymongo.mongo_client import MongoClient
import pandas as pd
import json
url="mongodb+srv://passworddivya:nandikole@cluster0.eqiou.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#create a new client
client=MongoClient(url)
#create database name and collection name
database_name="pwskills"
collection_name="waferfault"

df=pd.read_csv("C:\Users\Admin\sensorDetect\notebooks\wafer_23012020_041211.csv")
df.head()

df=df.drop("Unnamed: 0",axis=1)

jason_record=list(json.loads(df.T.to_json()).values())
client[database_name][collection_name].insert_many(jason_record)