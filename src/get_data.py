# Read The Parameters
# Process it
# Returns the data frame

import os
import yaml
import pandas as pd
import argparse

def read_params(config_path):        # Reading the parameters
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config


def get_data(config_path):
    config=read_params(config_path) # Read the parameters
    #print(config)
    data_path=config['data_source']['s3_source']  # Read the data path,from params.yaml
    df=pd.read_csv(data_path,sep=",",encoding='utf-8') # sep=separator
    print(df)

if __name__=="__main__":   # Entrance point of the project
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    data=get_data(config_path=parsed_args.config)
    





