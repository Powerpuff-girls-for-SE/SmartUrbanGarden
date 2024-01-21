import paho.mqtt.client as mqtt
import influxdb_client
import configparser
from influxdb_client.client.write_api import SYNCHRONOUS

config = configparser.ConfigParser()
config.read('config.ini')


def dbWrite(topic : str, value: int):
        
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
        measurement = topic[0]
        if measurement == 'garden':
            tag = topic[1]
            field = topic[2]
            p = influxdb_client.Point(measurement).tag("garden_area",tag).field(field, float(value))
        else:
            field = topic[1]
            p = influxdb_client.Point(measurement).field(field, float(value))
        write_api.write(bucket=bucket_name, org=org, record=p)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("garden/#")
    # client.subscribe("garden/#/temperature")
    # client.subscribe("garden/#/humidity")
    # client.subscribe("garden/#/moisture")
    

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print(str(msg.topic + " -> " + payload))
    dbWrite(str(msg.topic), payload)

def main():
    mqtt_client = mqtt.Client(client_id="monitor", reconnect_on_failure=True)
    mqtt_client.connect(config['mqtt']['broker'], int(config['mqtt']['port']))
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.loop_forever()

if __name__ == '__main__':
    main()