# load the train and test
# train the algorithm
# save the metrics and parameters

import os
import warnings
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from get_data import read_params
import argparse
import joblib
import json

# function creation for calculating the values
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2





def train_and_evaluate(config_path):
    config=read_params(config_path)
    test_data_path=config["split_data"]["test_path"]
    train_data_path=config["split_data"]["train_path"]
    random_state=config["base"]["random_state"]
    model_dir= config["model_dir"] # where we are going to save the model
    alpha= config["estimators"]["ElasticNet"]["params"]["alpha"] # Parameters
    l1_ratio= config["estimators"]["ElasticNet"]["params"]["l1_ratio"] # Parameters
    target= [config["base"]["target_col"]] # output column

    train = pd.read_csv(train_data_path,sep=",") # Read the train file
    test = pd.read_csv(test_data_path,sep=",") # Read the test file

    # Dependent Columns
    train_y=train["TARGET"]
    test_y=test["TARGET"]

    # Independent columns
    train_x=train.drop("TARGET",axis=1)
    test_x=test.drop("TARGET",axis=1)

    lr=ElasticNet(
        alpha=alpha,
        l1_ratio=l1_ratio,
        random_state=random_state)
    
    # fit the model
    lr.fit(train_x,train_y)

    # Prediction

    predicted_qualities=lr.predict(test_x)

    # calculate the  values 
    (rmse,mae,r2)=eval_metrics(test_y,predicted_qualities)
    print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)

# Report need to be added in src file
    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]

    with open(scores_file, "w") as f: # Open the scores file
        scores = {                      # Creating dictionary to store score
            "rmse": rmse,
            "mae": mae,
            "r2": r2
        }
        json.dump(scores, f, indent=4) # to store the data we need to dump,scores.files,indentation

    with open(params_file, "w") as f:   # Creating dictionary to store params
        params = {
            "alpha": alpha,
            "l1_ratio": l1_ratio,
        }
        json.dump(params, f, indent=4)

    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")

    joblib.dump(lr, model_path) # model create
    
    
    
if __name__=="__main__":   # Entrance point of the project, also to check the outcome
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)





