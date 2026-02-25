import os
import sys
from src.exception import CustomException
import pandas as pd
from src.logger import logging



from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig, ModelTrainer


@dataclass
class DataIngestionConfig:  # this is the class that tells where our data will be stored.
    """
    dataclasses: a Python library that helps us make classes that mainly store data.
    So this dataclass is like a box of addresses where we keep track of where our data files live.
    @dataclass: tells Python “this class is a dataclass.” It will automatically make an __init__ method (constructor) 
    and a nice __repr__ (string display).
    """
    train_data_path: str=os.path.join('artifacts', "train.csv") #  a variable that stores the location(path) of the training data file (artifacts/train.csv).
    test_data_path: str=os.path.join('artifacts', "test.csv")   # stores the location(path) of the test data file (artifacts/test.csv).
    raw_data_path: str=os.path.join('artifacts', "data.csv")    # stores the location(path) of raw data (artifacts/train.csv).
    # os.path.join(...): safely combines folder names and file names into a full path according to the current os system.

# This is the class that tells how we prepare the data and stored it
class DataIngestion:   
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # Now we have access to all the above paths created using self.ingestion_config variable

    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion method or component")
        try:
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the dataset as dataframe")

            # os.path.dirname()--> Extract folder only i.e artifacts, (2) os.makedirs()-->Creates folder. exist_ok=True --> Will not through error if already exist.
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) # Create a directory with a name artifacts

            # Svae the df with name data.csv in the path/location artificats directory. 
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True) 
            
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            # train_test_split(df)  (1)→ Used in Data Ingestion.  (2)→ Splits whole dataset,      (3) Single parameter passed 2 vairables return

            # train_test_split(X, y) (1) Used in Model Training   (2)→ Splits features & labels   (3) Two paramter is passed 4 vairables return

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header= True)
            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
        

if __name__=="__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transforamtion = DataTransformation()
    train_arr, test_arr, _ = data_transforamtion.initiate_data_transformation(train_data, test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
            
