import requests
from flask import Flask
from flask import jsonify
from flask import request
import configparser
 
config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.secret_key = config.get('flask', 'SECRET_KEY')

@app.route("/planner/check_measurements", methods=["POST"])
def check_measurements():
    measurements = request.json

    for area, values in measurements.items():
        for measurement, value in values.items():
            action = check_action(measurement, value)
            print(f"In area '{area}', for measurement '{measurement}', action: {action}")

    resp = jsonify(success=True, error="none")
    resp.status_code = 200
    return resp

def check_action(measurement, value):
    if measurement == 'light':
        if value < 100:
            return 'Increase light'
        elif value > 800:
            return 'Decrease light'
    elif measurement == 'temperature':
        if value < 18:
            return 'Increase temperature'
        elif value > 25:
            return 'Decrease temperature'
    elif measurement == 'soil_moisture':
        if value < 30:
            return 'Turn water pump on'
        elif value > 70:
            return 'Turn water pump off'
    elif measurement == 'humidity':
        if value < 40:
            return 'Increase humidity'
        elif value > 80:
            return 'Decrease humidity'
    
    # Default action if no specific condition is met
    return 'No action needed'

if __name__ == "__main__":
    app.run(debug=True, host='173.20.0.105', port=5007)