import numpy as np
from flask import Flask, request, jsonify, render_template

import requests
import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "puYxlBXzc8bCOJBEKcpSk8ZC-w9D97xSMvQiOh2y1wQN"

token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line

   
app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('CKD.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    
    age=request.form["age"]
    bp=request.form["bp"]
    sg=request.form["sg"]
    al=request.form["al"]
    au=request.form["su"]
    rbc=request.form["rbc"]
    pc=request.form["pc"]
    pcc=request.form["pcc"]
    ba=request.form["ba"]
    bgr=request.form["bgr"]
    bu=request.form["bu"]
    sc=request.form["sc"]
    sod=request.form["sod"]
    pot=request.form["pot"]
    hemo=request.form["hemo"]
    pcv=request.form["pcv"]
    wc=request.form["wc"]
    rc=request.form["rc"]
    ht=request.form["htm"]
    dm=request.form["dm"]
    cad=request.form["cad"]
    appet=request.form["appet"]
    pe=request.form["pe"]
    ane=request.form["ane"]
    
    payload_scoring = {"input_data": [{"field": [['age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr', 'bu',
       'sc', 'sod', 'pot', 'hemo', 'pcv', 'wc', 'rc', 'htn', 'dm', 'cad',
       'appet', 'pe', 'ane']], "values": [[25,60,1.02,0,0,0,0,0,0,119,27,0.5,137.53,4.63,15.2,40,9200,5.2,0,0,0,1,0,0
]]}]}
                                        
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/23a45911-67a8-4070-be72-46c6eaa3fda7/predictions?version=2022-11-12', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    prediction=response_scoring.json()
    print(prediction)

    pred=prediction['predictions'][0]['values'][0][0]
 
    if(pred == 0):
        output=False
        print("Patient does not has ckd")
       
    
    else:
        output=True
        print("Patient has  ckd")
    
    if(output ==False):
       return render_template('positive.html')
    else:
       return render_template('negative.html')
    

if __name__ == "__main__":
    app.run(debug=True)
    
    