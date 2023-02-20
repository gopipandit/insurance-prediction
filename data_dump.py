import pymongo
import pandas as pd
import json

client = pymongo.MongoClient('localhost', 27017)
db = client['mydb']
col = db['training_data']


DATA_FILE_NAME = (r"D:\ML_Project\Insurance_prediction\insurance-prediction\insurance.csv")
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_NAME)
    print(f"Rows and Columns: {df.shape}")

    df.reset_index(drop=True, inplace= True)

    json_record = list(json.loads(df.T.to_json()).values())


    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

