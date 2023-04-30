import os
from datetime import datetime
from src.exception import CustomException
from src.logger import logging

file_name="insuranceFraud.csv"
train_file_name="train.csv"
test_file_name="test.csv"
class TrainingPipelineConfig():
    def __init__(self):
        self.artifact_dir=os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")

class DataIngestionConfig():
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.database_name="Insurance"
        self.collection_name="Fraud_detection"
        self.data_ingestion_dir=os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
        self.feature_store_file_path=os.path.join(self.data_ingestion_dir,"feature_store_dir")
        self.train_file_path=os.path.join(self.data_ingestion_dir,"dataset",train_file_name)
        self.test_file_path = os.path.join(self.data_ingestion_dir, "dataset", test_file_name)
        self.test_size=0.2

    def to_dict(self)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise CustomException(e,sys)
class DataValidationConfig():
    pass
class DataTransformationConfig():
    pass
class ModelTrainerConfig():
    pass
class ModelEvaluationConfig():
    pass
class ModelPusherConfig():
    pass