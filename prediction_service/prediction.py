
import yaml
import numpy as np
import joblib
import os
import json


params_path="params.yaml"
schema_path=  os.path.join("prediction_service","schema_in.json") # schema_in.json

# Not in Range
class NotInRange(Exception):
    def __init__(self,message="Values Entered Are not in range"):
        self.message=message
        super().__init__(self.message) # Print The message

# Not in Column(If a person enters a wrong column)
class NotInCols(Exception):
    def __init__(self,message="Not in Columns"):
        self.message=message
        super().__init__(self.message) # Print The message 



def read_params(config_path=params_path):        # Reading the parameters
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config


def predict(data):
    config=read_params(params_path)
    model_dir_path=config["webapp_model_dir"] # this is present in params, so we need to transfer the model from (saved_models) to (prediction_service\model\model.joblib) for the prediction
    model= joblib.load(model_dir_path) # Loading the model
    prediction=model.predict(data).tolist()[0] # Predict the thing and convert it into list,[0] # SO that we will not get converted to list format
    
    try:
        if 3<= prediction <= 8: # We are restricting it as we can see the TARGET Column
            return prediction
        else:
            raise NotInRange
    except NotInRange:
        return "Unxpected Result"
    
# Let's Call the schema part

def get_schema(schema_path=schema_path):
    with open(schema_path) as json_file:
        schema=json.load(json_file) # It will read the schema
    return schema


# We will do the validation path
def validate_input(dict_request):     # This will come from API Response(api_response)

    def _validate_cols(col):        # It takes the column part
        schema=get_schema()
        actual_col=schema.keys()  # Call the actual values
        if col not in actual_col:     # If the columns are not in actual column
            raise NotInCols
        

    def _validate_values(col,val):  # we require col and values to compare it
        schema=get_schema()
        if not (schema[col]["min"] <= float(dict_request[col]) <= schema[col]["max"]):     # set the range, dict_request coming from webapp or api
            raise NotInRange

    for col,val in dict_request.items():          # For column and values, when you call items list of tuple
        _validate_cols(col)  # Validate the columns
        _validate_values(col,val)   # Validate the values and range
    return True                        # If Every thing is true, then only it will return



    
# If the request is coming from the webapp
def form_response(dict_request):
    if validate_input(dict_request):
        data=dict_request.values() # Converting to values
        data= [list(map(float,data))]  # Values are coming from webapp in form of string,we will use map to convert and convert to list
        response=predict(data)
        return response

    

# If the request is coming from the api
def api_response(dict_request):  # It is called in setup
    try:
        if validate_input(dict_request):
            data=np.array([list(dict_request.values())]) # Pass the data , convert to list and then array
            response = predict(data) # Getting the response in 2D List and getting the response
            response={"response": response}# Since It is a json so we will Converted to dictionary and then it will pass as json response
            return float(response)
        
    except NotInRange as e:
        response = {"the_exected_range": get_schema(), "response": str(e) }
        return response

    except NotInCols as e:
        response = {"the_exected_cols": get_schema().keys(), "response": str(e) }
        return response
    except Exception as e:
        response={"The Expected range":get_schema(),"response":str(e)} # Print the expected range, converted to string (e) 
        return response