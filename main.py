import sys 
import os 
from src.exception import SensorException  
from src.logger import logging 
from src.utils import dump_csv_file_to_mongodb_collection

if __name__ == "__main__":
     file_path = "E:/PRINCE Folder/ML-and-Data-Science-Projects/ML-Project/livesensor_for_APS/aps_failure_training_set1.csv" 
     database_name = "livesensor" 
     collection_name = "sensor" 
     dump_csv_file_to_mongodb_collection(file_path , database_name , collection_name)