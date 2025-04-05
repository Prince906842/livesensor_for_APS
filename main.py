import sys 
import os 
from src.exception import SensorException  
from src.logger import logging 


if __name__ == "__main__":

    try: 
        logging.info("the execution has started")
        a=1/0
    except Exception as e: 
        raise SensorException(e,sys)