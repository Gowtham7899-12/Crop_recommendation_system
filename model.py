# -*- coding: utf-8 -*-
#import libraries
import numpy as np
import requests , json
from flask import Flask, render_template,request
import http.client
import pickle#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('./index.html')


@app.route('/form')
def form():
    return render_template('./form.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    # print(final_features)
    prediction = model.predict(final_features)
    output = prediction 
    return render_template('./result.html', prediction_text=f'{output[0].capitalize()}')



@app.route('/weather', methods= ['POST', 'GET'])
def weather():
    print(request.method)
    if request.method == "POST":
        location = request.form.get("place")
        print(location)
        api_key ='03b1acbfd0387ac994dad57eb102fe01'
        
        link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
        api_link = requests.get(link)
        data = api_link.json()
        # print(data)
        temp= round((data['main']['temp'])-273.15,2)
        humidity=data['main']['humidity']
        pressure1=data['main']['pressure']
        # weather_desc = data['weather'][0]['description'].capitalize()
        wind_speed = data['wind']['speed']
        place =data['name']
        # return render_template('./weather.html', info=data,tempr=temp,desc=weather_desc,speed=wind_speed,humid=humidity,pressure=pressure1,placeo=place)
    else:
        api_key ='03b1acbfd0387ac994dad57eb102fe01'
        location = 'Kolar'
        link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
        api_link = requests.get(link)
        data = api_link.json()
            # print(data)
        temp= round((data['main']['temp'])-273.15,2)
        humidity=data['main']['humidity']
        pressure1=data['main']['pressure']
        # weather_desc = data['weather'][0]['description'].capitalize()
        wind_speed = data['wind']['speed']
        place =data['name']
    return render_template('./weather.html', info=data,tempr=temp,speed=wind_speed,humid=humidity,pressure=pressure1,placeo=place)
if __name__ == "__main__":
    app.run(debug=True)
