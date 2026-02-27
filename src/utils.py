import os
import sys

import numpy as np 
import pandas as pd
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException


def save_object(file_path, obj): # when doing transformation but also used at training stage
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



def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))): # 
            model = list(models.values())[i] # From a list of models give the i-th index model(value), modlels.values()[i]---> Gives the model itself.
            para=param[list(models.keys())[i]]  # give list of keys of i-th key()

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score # model.keys()[i] ---> It gives the model name

        return report

    except Exception as e:
        raise CustomException(e, sys)


# This is for without Hyperparameter tuning.
# def evaluate_models(X_train, y_train, X_test, y_test, models): # when tarinig a model
#     try:
#         report = {}

#         for name, model in models.items():
#             # Train Model
#             model.fit(X_train, y_train)

#             y_train_pred = model.predict(X_train)
#             y_test_pred = model.predict(X_test)

#             train_model_score = r2_score(y_train, y_train_pred)
#             test_model_score = r2_score(y_test, y_test_pred)
#             report[name] = test_model_score

#         return report
    
    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise CustomException(e, sys)
