from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('heart_disease_random_forest_model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


#standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    #Fuel_Type_Diesel=0
    if request.method == 'POST':
        Age = int(request.form['Age'])
        Gender=request.form['sex']
        if(Gender=='Male'):
            Gender=1
        else:
            Gender=0	
        Cp = int(request.form['cp'])
        Trestbps = int(request.form['trestbps'])
        Chol = int(request.form['chol'])
        Fbs = int(request.form['fbs'])
        Restecg = int(request.form['restecg'])
        Thalach = int(request.form['thalach'])
        Exang = int(request.form['exang'])
        Oldpeak=float(request.form['oldpeak'])
        Slope=int(request.form['slope'])
        Ca=int(request.form['slope'])
        Thal=int(request.form['slope'])
        prediction=model.predict([[Age,sex,cp,tresttbps,chol,fbs,restecg,thalach,exang,oldspeak,slope,ca,thal]])
        output=round(prediction[0],2)
        if output==0:
            return render_template('index.html',prediction_text="Patient does not have heart disease")
        elif output==1:
            return render_template('index.html',prediction_text="Patient has heart disease")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

