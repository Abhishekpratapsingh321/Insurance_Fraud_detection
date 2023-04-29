import pandas as pd
from src.config import client
from src.logger import logging
from src.exception import CustomException
import os,sys

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    Description: this function return collection as dataframe
    :param database_name: database name
    :param collection_name: collection name
    :return: pandas dataframe
    """
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df=pd.DataFrame(list(client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id")
            df=df.drop("_id",axis=1)
        logging.info(f"Row and Column")
        return df
    except Exception as e:
        raise CustomException(e,sys)


