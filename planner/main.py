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
    url = 'http://172.100.0.16:5006'

    try:
        for area in measurements:
            for measurement in measurements[area]:
                print(f'\nArea: {area}, Measurement: {measurement}, Condition: {measurements[area][measurement]}')
                new_url = f'{url}/{area}/{measurement}'

                if measurements[area][measurement] == "Temperature low":
                    x = requests.get(f'{new_url}/on')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} should increase.')

                elif measurements[area][measurement] == "Temperature high":
                    x = requests.get(f'{new_url}/on')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} should decrease.')

                elif measurements[area][measurement] == "Temperature optimal":
                    x = requests.get(f'{new_url}/off')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} is optimal.')

                elif measurements[area][measurement] == "Humidity low":
                    alarm_url = f'{url}/{area}/high'
                    x = requests.get(alarm_url)
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} should increase.')

                elif measurements[area][measurement] == "Humidity high":
                    alarm_url = f'{url}/{area}/low'
                    x = requests.get(alarm_url)
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} should decrease.')

                elif measurements[area][measurement] == "Humidity optimal":
                    alarm_url = f'{url}/{area}/off'
                    x = requests.get(alarm_url)
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} is optimal.')

                elif measurements[area][measurement] == "Light low":
                    alarm_url = f'{url}/{area}/high'
                    x = requests.get(alarm_url)
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} should increase.')

                elif measurements[area][measurement] == "Light high":
                    alarm_url = f'{url}/{area}/low'
                    x = requests.get(alarm_url)
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} should decrease.')

                elif measurements[area][measurement] == "Light optimal":
                    alarm_url = f'{url}/{area}/off'
                    x = requests.get(alarm_url)
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} is optimal.')

                elif measurements[area][measurement] == "Moisture low":
                    x = requests.get(f'{new_url}/on')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} should increase.')

                elif measurements[area][measurement] == "Moisture high":
                    x = requests.get(f'{new_url}/on')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} should decrease.')

                elif measurements[area][measurement] == "Moisture optimal":
                    x = requests.get(f'{new_url}/off')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} is optimal.')

    except Exception as exc:
        print(exc)

    resp = jsonify(success=True, error="none")
    resp.status_code = 200
    return resp
    

if __name__ == "__main__":
    app.run(debug=True, host='172.100.0.16', port=5007)