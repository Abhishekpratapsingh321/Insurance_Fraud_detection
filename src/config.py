import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os


@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("mongo_db_url")

env_var = EnvironmentVariable()
#provide the mongodb localhost url to connect to python mongodb
client = pymongo.MongoClient(env_var.mongo_db_url)
