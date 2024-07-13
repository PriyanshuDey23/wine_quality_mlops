# Read the data from data source
# Save it in the data/raw for further process

import os
from get_data import read_params,get_data # get data will return the data frame,get params will give the parameters
import argparse

def load_and_save(config_path):   # expect configration file
    config=read_params(config_path)   # read the parameters
    df=get_data(config_path)
    # if there some in between words space, in between the column heading , so we are going to fix it
    new_cols=[col.replace(" ","_") for col in df.columns] # Replace space with _
    raw_data_path=config["load_data"]["raw_dataset_csv"] # check params .yaml
    # save the data
    df.to_csv(raw_data_path,sep=",",index=False,header=new_cols)
    #print(new_cols)

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    load_and_save(config_path=parsed_args.config)

#file is saved into Data/processed

