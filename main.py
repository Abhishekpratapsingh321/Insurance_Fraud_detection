from src.logger import logging
from src.exception import CustomException
import os,sys
from src.utils import get_collection_as_dataframe



if __name__=="__main__":
    try:
        get_collection_as_dataframe(database_name="Insurance",collection_name="Fraud_detection")
    except Exception as e:
        print(e)
