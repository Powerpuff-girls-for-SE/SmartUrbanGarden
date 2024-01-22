import paho.mqtt.client as mqtt
import influxdb_client
import configparser
import traceback
from influxdb_client.client.write_api import SYNCHRONOUS

config = configparser.ConfigParser()
config.read('config.ini')


def write_to_influxdb(topic : str, value: int):
    # influxdb
    org = config['influxdb']['ORG']
    bucket_name = config['influxdb']['BUCKET_NAME']

    db_client = influxdb_client.InfluxDBClient(
        url=config['influxdb']['URL'],
        token=config['influxdb']['TOKEN'],
        org=org
    )
    write_api = db_client.write_api(write_options=SYNCHRONOUS)

    #data formatting and storing
    topic = topic.split("/")
    topic_header = topic[0]
    garden_area = topic[1]
    sensor = topic[2]
    p = influxdb_client.Point(topic_header).tag("garden_area", garden_area).field(sensor, float(value))
    write_api.write(bucket=bucket_name, org=org, record=p)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("garden/#")
    

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print("Message written to influxdb")
    print(str(msg.topic + " -> " + payload))
    write_to_influxdb(str(msg.topic), payload)

def main():
    mqtt_client = mqtt.Client(client_id="monitor", reconnect_on_failure=True)
    mqtt_client.connect(config['mqtt']['broker'], int(config['mqtt']['port']))
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.loop_forever()
    try:
        mqtt_client = mqtt.Client(client_id="Monitor", reconnect_on_failure=True)
        mqtt_client.connect("172.100.0.13", 1883)
        mqtt_client.on_connect = on_connect
        mqtt_client.on_message = on_message
        mqtt_client.loop_forever()
    except:
        print(traceback.format_exc())
         

if __name__ == '__main__':
    main()