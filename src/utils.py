import pandas as pd 
import logging 
import json 
from src.config import mongoClient 

def dump_csv_file_to_mongodb_collection(filepath:str , database_name:str ,collection_name:str) -> None:   
    try: 
        df = pd.read_csv(filepath) 
        df.reset_index(drop=True ,inplace=True) 
        json_records = list(json.loads(df.T.to_json()).values()) 
        mongoClient[database_name] [collection_name].insert_many(json_records)
    except Exception as e: 
        print(e)

