# Here we will write all the flusk function and create the app
from flask import Flask,render_template,request,jsonify
import os
import yaml
import joblib
import numpy as np
from prediction_service import prediction



webapp_root= "webapp" # Web app root 

static_dir= os.path.join(webapp_root,"static") # Static Directory path along with static folder
template_dir= os.path.join(webapp_root,"templates") # Template Directory along wih templates folder

app=Flask(__name__,static_folder=static_dir,template_folder=template_dir)



# Now create a root
@app.route("/", methods=["GET","POST"]) # Both the methods
def index():
    if request.method == "POST":
        try:                                   # we need to render the 404 
            if request.form:                    # If request is coming from web app
                data_req=dict(request.form)      # Data Requested
                response=prediction.form_response(data_req)  # FOrm response and api response is a funstion
                return render_template("index.html",response=response)
            elif request.json:                               # If request is coming from an API
                response = prediction.api_response(request.json) # We will call the api response in dict format
                return jsonify(response)                        # It will get converted into a json format

        except Exception as e:
            print(e)
            error= {"error": "Something Went Wrong !! Try again"}   # Pass the error message
            error={"error":e}  # we have to pass this in json format
            return render_template("404.html",error=error)                  # Print The error straightly
    else:
        return render_template("index.html")
    
    


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)



