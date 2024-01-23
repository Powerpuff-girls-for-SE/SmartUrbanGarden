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
    url = config['executor']['URL']

    try:
        for area in measurements:
            for measurement in measurements[area]:
                print(f'\nArea: {area}, Measurement: {measurement}, Condition: {measurements[area][measurement]}')
                new_url = f'{url}/{area}/{measurement}'

                if measurements[area][measurement] == config["sensor"]["LOW"]:
                    x = requests.get(f'{new_url}/on')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} should increase.')

                elif measurements[area][measurement] == config["sensor"]["HIGH"]:
                    x = requests.get(f'{new_url}/off')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} should decrease.')

                elif measurements[area][measurement] == config["sensor"]["OPTIMAL"]:
                    x = requests.get(f'{new_url}/off')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} is optimal.')

                elif measurements[area][measurement] == config["sensor"]["LOW"]:
                    x = requests.get(f'{new_url}/high')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} should increase.')

                elif measurements[area][measurement] == config["sensor"]["HIGH"]:
                    x = requests.get(f'{new_url}/low')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} should decrease.')

                elif measurements[area][measurement] == config["sensor"]["OPTIMAL"]:
                    x = requests.get(f'{new_url}/off')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} is optimal.')

                elif measurements[area][measurement] == config["sensor"]["LOW"]:
                    x = requests.get(f'{new_url}/high')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} should increase.')

                elif measurements[area][measurement] == config["sensor"]["HIGH"]:
                    x = requests.get(f'{new_url}/low')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} should decrease.')

                elif measurements[area][measurement] == config["sensor"]["OPTIMAL"]:
                    x = requests.get(f'{new_url}/off')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} is optimal.')

                elif measurements[area][measurement] == config["sensor"]["LOW"]:
                    x = requests.get(f'{new_url}/on')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} should increase.')

                elif measurements[area][measurement] == config["sensor"]["HIGH"]:
                    x = requests.get(f'{new_url}/on')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} should decrease.')

                elif measurements[area][measurement] == config["sensor"]["OPTIMAL"]:
                    x = requests.get(f'{new_url}/off')
                    print(f'{measurement} measurement: {measurements[area][measurement]}. {measurement} is optimal.')

    except Exception as exc:
        print(exc)

    resp = jsonify(success=True, error="none")
    resp.status_code = 200
    return resp
    

if __name__ == "__main__":
    app.run(debug=True, host=config['planner']['host'], port=int(config['planner']['port']))