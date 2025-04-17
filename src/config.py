from dataclasses import dataclass 
import os 
import pymongo 

@dataclass 

class EnvironmentVariabale: 
  mongo_db_url:str = os.getenv("MONGO_DB_URL") 

env_var = EnvironmentVariabale() 

mongoClient = pymongo.MongoClient(env_var.mongo_db_url)