import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

## import ridge regression and standard scaler pickle
ridge_model = pickle.load(open(r'D:\GitHub\DataScience-ML-DL-NLP-Projects-Practice\19_Machine Learning\4_ Steps By Step Project Implementation With LifeCycle OF ML Project\ML Project Deployment in AWS\models\ridge.pkl', 'rb'))
standard_scaler = pickle.load(open(r'D:\GitHub\DataScience-ML-DL-NLP-Projects-Practice\19_Machine Learning\4_ Steps By Step Project Implementation With LifeCycle OF ML Project\ML Project Deployment in AWS\models\scaler.pkl', 'rb'))


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata')
def predict_datapoint():
    if request.method =="POST":
        Temperature= float(request.form.get('Temperature'))
        RH  = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        
        new_data_scaled =  standard_scaler.transfrom([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes,Region]])
        result = ridge_model.predict(new_data_scaled)
        
        return render_template('home.html', result = result[0])
    else:
        return render_template('home,html')
    
if __name__ == '__main__':
    app.run(host="0.0.0.0")