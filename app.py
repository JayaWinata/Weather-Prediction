from flask import Flask, render_template, request, abort
from prometheus_client import Histogram, Counter, generate_latest, Gauge
import os
import requests
import time
import numpy as np
import pandas as pd
from src.pipeline.prediction_pipleine import PredictionPipeline
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
SHARED_KEY = os.getenv('PROMETHEUS_HEX') # Shared key for Prometheus

# Counter to count endpoint clicks
endpoint_clicks = Counter('endpoint_clicks', 'Total clicks per endpoint', ['endpoint'])

# Histogram to track response times
endpoint_latency = Histogram('endpoint_latency_seconds', 'Endpoint response time', ['endpoint'])

# Counter to track unique user locations
user_locations = Counter('unique_user_locations', 'Unique user locations', ['latitude', 'longitude'])

# Counter to track errors
error_counter = Counter('endpoint_errors', 'Total errors per endpoint and status code', ['endpoint', 'status_code'])

# Histogram to track request sizes
request_size = Histogram('request_size_bytes', 'Request size in bytes', ['endpoint'])

# Histogram to track response sizes
response_size = Histogram('response_size_bytes', 'Response size in bytes', ['endpoint'])

# Gauge to track active requests
active_requests = Gauge('active_requests', 'Number of active requests')

# Histogram to track database query times
db_query_time = Histogram('db_query_time_seconds', 'Database query time')

# Custom business metric example: Counter to track user signups
user_signups = Counter('user_signups', 'Total user signups')

def get_location(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        if data['status'] == 'success':
            return [data['lat'], data['lon']]
        else:
            return [0.0, 0.0]
    except Exception:
        return [0.0, 0.0]

@app.before_request
def start_timer():
    request.start_time = time.time()
    active_requests.inc()

@app.after_request
def track_metrics(response):
    if request.path.startswith("/static/") or response.direct_passthrough:
        return response

    if request.path != '/favicon.ico' and request.path != '/metrics':
        endpoint_clicks.labels(endpoint=request.path).inc()
        request_latency = time.time() - request.start_time
        endpoint_latency.labels(endpoint=request.path).observe(request_latency)
        request_size.labels(endpoint=request.path).observe(len(request.data))
        response_size.labels(endpoint=request.path).observe(len(response.data))
    active_requests.dec()
    return response

@app.errorhandler(Exception)
def handle_exception(e):
    error_counter.labels(endpoint=request.path, status_code="500").inc()
    active_requests.dec()
    return "Internal Server Error", 500

@app.errorhandler(404)
def page_not_found(e):
    error_counter.labels(endpoint=request.path, status_code="404").inc()
    active_requests.dec()
    return "404 Not Found", 404

@app.errorhandler(403)
def page_not_found(e):
    error_counter.labels(endpoint=request.path, status_code="403").inc()
    active_requests.dec()
    return "403 Forbidden", 403

@app.route('/metrics')
def metrics():
    try:
        return generate_latest(), 200, {'Content-Type': 'text/plain'}
    except Exception as e:
        app.logger.error("Error generating metrics: %s", str(e))
        abort(500)  # Internal Server Error

@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')

@app.route('/train', methods=['GET'])
def training():
    print('training pipeline running...')
    os.system("python main.py")
    print('training pipeline finished')
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