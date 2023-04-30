import pandas as pd

from src import utils
from src.entity import config_entity
from src.entity import artifact_entity
from src.exception import CustomException
from src.logger import logging
import os,sys
import numpy as np
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self,data_ingestion_config:config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            logging.info(f"Exporting collection data as pandas dataframe")

            df:pd.DataFrame()=utils.get_collection_as_dataframe(
                database_name=self.data_ingestion_config.database_name,
                collection_name=self.data_ingestion_config.collection_name)

            logging.info(f"list of columns not necessary for prediction")
            cols_to_drop = ['policy_number', 'policy_bind_date', 'policy_state', 'insured_zip', 'incident_location',
                            'incident_date']
            logging.info(f"dropping the unnecessary columns")
            df.drop(columns=cols_to_drop, inplace=True)

            logging.info(f"save data in feature store")
            df.replace(to_replace="?",value=np.NAN,inplace=True)

            logging.info(f"create feature store folder")
            feature_store_dir=os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir,exist_ok=True)

            logging.info(f"save df to feature store folder")
            df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_path,index=False,header=True)

            logging.info(f"split dataset into train and test set")
            train_df,test_df=train_test_split(df,test_size=self.data_ingestion_config.test_size)

            logging.info(f"create dataset directory folder if not available")
            dataset_dir=os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dataset_dir,exist_ok=True)

            logging.info(f"save df to feature store folder")
            train_df.to_csv(path_or_buf=self.data_ingestion_config.train_file_path)
            test_df.to_csv(path_or_buf=self.data_ingestion_config.test_file_path)

            logging.info(f"prepare artifact")
            data_ingestion_artifact=artifact_entity.DataIngestionArtifact(
                feature_store_file_path=self.data_ingestion_config.feature_store_file_path,
                train_file_path=self.data_ingestion_config.train_file_path,
                test_file_path=self.data_ingestion_config.test_file_path
            )

            return data_ingestion_artifact


        except Exception as e:
            raise CustomException(e,sys)
