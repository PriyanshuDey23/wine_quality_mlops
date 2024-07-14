# SPlit the raw data 
# save it in data\processed

import os
import pandas as pd
from sklearn.model_selection import train_test_split
import argparse
from get_data import read_params # Read the parameters

def split_and_saved_data(config_path):
    config=read_params(config_path)  # once read this data,check the params yaml to check the parameters
    test_data_path = config["split_data"]["test_path"]  # we need a test data
    train_data_path = config["split_data"]["train_path"]  # we need a train data
    raw_data_path= config["load_data"]["raw_dataset_csv"] # From where we are going to read the dataset
    split_ratio=config["split_data"]["test_size"]
    random_state=config["base"]["random_state"]

    df=pd.read_csv(raw_data_path, sep="," )
    train,test=train_test_split(
        df,
        test_size=split_ratio,
        random_state=random_state)
    
    # save in the format of csv
    train.to_csv(train_data_path,sep=",",index=False,encoding="utf-8") # path the path inside the the bracket
    test.to_csv(test_data_path,sep=",",index=False,encoding="utf-8")

   
if __name__=="__main__":   # Entrance point of the project, also to check the outcome
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    split_and_saved_data(config_path=parsed_args.config)