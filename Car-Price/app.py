from flask import Flask, render_template, request
#import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Car Price Prediction.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Year = int(request.form['Year'])
        #Present_Price=float(request.form['Present_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        #Kms_Driven2=np.log(Kms_Driven)
        Owner=int(request.form['Owner'])
        Mileage=float(request.form['Mileage'])
        Engine=float(request.form['Engine'])
        Power = float(request.form['Power'])
        Seats=int(request.form['Seats'])
        
        Fuel_Type=request.form['Fuel_Type']
        if(Fuel_Type=='CNG'):
                Fuel_Type_Diesel=0
                Fuel_Type_LPG=0
                Fuel_Type_Petrol=0
                
        elif(Fuel_Type=='Diesel'):
                Fuel_Type_Diesel=1
                Fuel_Type_LPG=0
                Fuel_Type_Petrol=0
                
        elif(Fuel_Type=='LPG'):
                Fuel_Type_Diesel=0
                Fuel_Type_LPG=1
                Fuel_Type_Petrol=0
                
        else:
            Fuel_Type_Diesel=0
            Fuel_Type_LPG=0
            Fuel_Type_Petrol=1
            
     
        Year=2020-Year
      
        Transmission_Mannual=request.form['Transmission']
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0
        prediction=model.predict([[Year,Kms_Driven,Owner,Mileage,Engine,Power,Seats,Fuel_Type_Diesel,Fuel_Type_LPG,Fuel_Type_Petrol,Transmission_Mannual]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Unexpected ! Price is less then Zero.")
        else:
            return render_template('index.html',prediction_text="The Car Price is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

