import pandas as pd
import numpy as np
import pymongo
import os
from insurance.exception import InsuranceException
from insurance.config import mongo_client
from insurance.logger import logging


# client = pymongo.MongoClient('localhost', 27017)
# db = client['mydb']
# col = db['training_data']


def get_collection_as_dateframe(database_name:str, collection_name:str):
    try:
        logging.info(f"reading data from database- {database_name} and collection- {collection_name}")
        df = pd.DataFrame(mongo_client[database_name][collection_name].find())
        logging.info(f"Found columns: {df.columns}")
        if '_id' in df.columns:
            logging.info("Dropping column id")
            df.drop('_id', axis= 1)
        logging.info(f"rows and columns in the data{df.shape}")
        return df
    except Exception as e:
        raise InsuranceException(e, sys)