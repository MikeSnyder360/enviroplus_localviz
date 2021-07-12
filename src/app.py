import os
import time
from flask import Flask, request, jsonify, render_template
from AirQualityMonitor import AirQualityMonitor
from apscheduler.schedulers.background import BackgroundScheduler
import redis
import atexit
from flask_cors import CORS, cross_origin



app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
aqm = AirQualityMonitor()

print("scheduler")
scheduler = BackgroundScheduler()
scheduler.add_job(func=aqm.save_measurement_to_redis, trigger="interval", seconds=1)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())


def reconfigure_data(measurement):
    """Reconfigures data for chart.js"""
    current = int(time.time())
    measurement = measurement[:30]
    print(measurement)
    measurement.reverse()
    return {
        'labels': [x['time'] for x in measurement],
        'pm10': {
            'label': 'pm10',
            'data': [x['measurement'][3] for x in measurement],
            'backgroundColor': '#cc0000',
            'borderColor': '#cc0000',
            'borderWidth': 3,
        },
        'pm2': {
            'label': 'pm2.5',
            'data': [x['measurement'][2] for x in measurement],
            'backgroundColor': '#42C0FB',
            'borderColor': '#42C0FB',
            'borderWidth': 3,
        },
    }

@app.route('/')
def index():
    """Index page for the application"""
    print(aqm.get_last_n_measurements())
    context = {
        'historical': reconfigure_data(aqm.get_last_n_measurements()),
    }
    return render_template('index.html', context=context)


@app.route('/api/')
@cross_origin()

def api():
    """Returns historical data from the sensor"""
    context = {
        'historical': reconfigure_data(aqm.get_last_n_measurements()),
    }
    return jsonify(context)


@app.route('/api/now/')
def api_now():
    """Returns latest data from the sensor"""
    context = {
        'current': aqm.get_measurement(),
    }
    return jsonify(context)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=int(os.environ.get('PORT', '8000')))
