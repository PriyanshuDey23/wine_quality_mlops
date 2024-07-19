# Here we will write all the flusk function and create the app
from flask import Flask,render_template,request,jsonify
import os
import yaml
import joblib
import numpy as np
from prediction_service import prediction


params_path="params.yaml" # Parameter path
webapp_root= "webapp" # Web app root 

static_dir= os.path.join(webapp_root,"static") # Static Directory path along with static folder
template_dir= os.path.join(webapp_root,"templates") # Template Directory along wih templates folder

app=Flask(__name__,static_folder=static_dir,template_folder=template_dir)

def read_params(config_path):        # Reading the parameters
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config

def predict(data):
    config=read_params(params_path)
    model_dir_path=config["webapp_model_dir"] # this is present in params, so we need to transfer the model from (saved_models) to (prediction_service\model\model.joblib) for the prediction
    model= joblib.load(model_dir_path) # Loading the model
    prediction=model.predict(data)
    print(prediction)
    return prediction[0] # SO that we will not get converted to list format

def api_response(request):
    try:
        data=np.array([list(request.json.values())]) # Convert to numpy array
        response=predict(data)
        response={"response":response}
        return response
    except Exception as e:
        print(e)
        error= {"error": "Something Went Wrong !! Try again"}
        return error



# Now create a root
@app.route("/", methods=["GET","POST"]) # Both the methods
def index():
    if request.method == "POST":
        try:                                   # we need to render the 404 
            if request.form:                    # If request is coming from web app
                data=dict(request.form).values()  # Get the values
                data=[list(map(float,data))]    # map the txt value with the help of float, 2D list created
                response=predict(data)
                return render_template("index.html",response=response)
            elif request.json:                               # If request is coming from an API
                response = api_response(request.json)
                return jsonify(response)                        # It will get converted into a json format

        except Exception as e:
            print(e)
            error= {"error": "Something Went Wrong !! Try again"}   # Pass the error message
            return render_template("404.html",error)
    else:
        return render_template("index.html")


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)



