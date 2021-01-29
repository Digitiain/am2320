import os
from flask import Flask, render_template

if os.environ.get("FLASK_ENV") != "development":
    import am2320

app = Flask(__name__)


@app.route('/')
def home():

    if os.environ.get("FLASK_ENV") == "development":
        return render_template('index.html', temperature="21", humidity="56")
    else: 
        sensor_readings = am2320.get_sensor_data()
        temperature = sensor_readings[0]
        humidity = sensor_readings[1]
        return render_template('index.html', temperature=temperature, humidity=humidity)


if __name__ == '__main__':
    app.run()