import paho.mqtt.client as mqtt
import influxdb_client
import pandas as pd
import configparser
from influxdb_client.client.write_api import SYNCHRONOUS

config = configparser.ConfigParser()
config.read('config.ini')

# influxdb
org = config['influxdb']['ORG']
bucket_name = config['influxdb']['BUCKET_NAME']

db_client = influxdb_client.InfluxDBClient(
    url=config['influxdb']['URL'],
    token=config['influxdb']['TOKEN'],
    org=org
)

def dbWrite(topic : str, value: int):
        
        write_api = db_client.write_api(write_options=SYNCHRONOUS)

        #data formatting and storing
        topic = topic.split("/")
        measurement = topic[0]
        if measurement == 'indoor':
            tag = topic[1]
            field = topic[2]
            p = influxdb_client.Point(measurement).tag("room",tag).field(field, int(value))
        else:
            field = topic[1]
            p = influxdb_client.Point(measurement).field(field, int(value))
        write_api.write(bucket=bucket_name, org=org, record=p)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("")

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print(str(msg.topic + " -> " + payload))
    dbWrite(str(msg.topic), payload)

def main():
    mqtt_client = mqtt.Client(client_id="monitor")
    mqtt_client.connect(config['mqtt']['broker'], int(config['mqtt']['port']))
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.loop_forever()

if __name__ == '__main__':
    main()