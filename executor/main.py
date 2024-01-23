import requests
import influxdb_client
from flask import Flask
from flask import jsonify
from tenacity import retry
import paho.mqtt.client as mqtt
from influxdb_client.client.write_api import SYNCHRONOUS

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.secret_key = config.get('flask', 'SECRET_KEY')

class MQTTClient:
    @retry()
    def __init__(self,client_id):
        self.client = mqtt.Client(client_id=client_id, reconnect_on_failure=True)
        self.client.on_publish = lambda client, userdata, mid: print("PUBLISH: ", mid)
        self.client.connect(config["mqtt"]["broker"])

    def on_connect(client, userdata, flags, rc):
        print('Executor connected to MQTT ')

    def publish(self, topic, msg):
        self.client.publish(topic, msg)

client = MQTTClient(client_id='Executor')

@app.route("/<garden_area>/<sensor>/<action>", methods=["GET"])
def run_actuator(garden_area, sensor, action):
    if sensor == 'temperature':
        client.publish(f'thermostat/{garden_area}/{action}', '')
    elif sensor == 'humidity':
        client.publish(f'humidifier/{garden_area}/{action}', '')
    elif sensor == 'light':
        client.publish(f'smartBulb/{garden_area}/{action}', '')
    else:
        client.publish(f'water_pump/{garden_area}/{action}', '')

    resp = jsonify(success=True, error="none")
    resp.status_code = 200
    return resp

if __name__ == "__main__":
    app.run(debug=True, host=config['executor']['host'], port=int(config['executor']['port']))