import os
import sys

import numpy as np 
import pandas as pd
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        # Extract directory name only
        dir_path = os.path.dirname(file_path)

        # Create only the folder
        os.makedirs(dir_path, exist_ok=True)

        # Save object
        with open(file_path, "wb") as file_obj:  # Wrie Binary(wb) file.
            dill.dump(obj, file_obj)             # Save the obj in the file file_obj(file name)

    except Exception as e:
        raise CustomException(e, sys)




