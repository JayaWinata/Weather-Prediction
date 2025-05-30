from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from src.pipeline.prediction_pipleine import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')

@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return render_template('train_notif.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        try:
            temperature_2m_max = float(request.form['temperature_2m_max'])
            temperature_2m_min = float(request.form['temperature_2m_min'])
            apparent_temperature_max = float(request.form['apparent_temperature_max'])
            apparent_temperature_min = float(request.form['apparent_temperature_min'])
            wind_speed_10m_max = float(request.form['wind_speed_10m_max'])
            wind_gusts_10m_max = float(request.form['wind_gusts_10m_max'])
            wind_direction_10m_dominant = float(request.form['wind_direction_10m_dominant'])
            shortwave_radiation_sum = float(request.form['shortwave_radiation_sum'])
            uv_index_max = float(request.form['uv_index_max'])
            daylight_duration = float(request.form['daylight_duration'])
            sunshine_duration = float(request.form['sunshine_duration'])
            et0_fao_evapotranspiration = float(request.form['et0_fao_evapotranspiration'])

            data = [
                temperature_2m_max,
                temperature_2m_min,
                apparent_temperature_max,
                apparent_temperature_min,
                wind_speed_10m_max,
                wind_gusts_10m_max,
                wind_direction_10m_dominant,
                shortwave_radiation_sum,
                uv_index_max,
                daylight_duration,
                sunshine_duration,
                et0_fao_evapotranspiration
            ]

            data = np.array(data).reshape(1, len(data))

            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('result.html', prediction = str(predict[0]))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'Something went wrong'

    else:
        return render_template('result.html', prediction = "There is no data to be predicted! Press the back butotn")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 8080)