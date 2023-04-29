import pymongo
import pandas as pd
import json

#provide the mongodb localhost url to connect to python mongodb
client = pymongo.MongoClient("mongodb+srv://Pratap:Pratap9821@cluster0.4pbpbn7.mongodb.net/?retryWrites=true&w=majority")

data_file_path = 'insuranceFraud.csv'
database_name = "Insurance"
collection_name = "Fraud_detection"

if __name__=="__main__":
    df = pd.read_csv(data_file_path)
    print(f"Rows and Cloumns: {df.shape}")


    #convert dataframe to json so that we can dump these recored in mongodb
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())

    print(json_record[0])
     #insert converted json record to mongo db
    client[database_name][collection_name].insert_many(json_record)