from paho.mqtt import client as mqtt_client
import influxdb_client
import configparser
from influxdb_client.client.write_api import SYNCHRONOUS

config = configparser.ConfigParser()
config.read('config.ini')


def write_to_influxdb(topic : str, value: float):
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

def connect_mqtt(client_id, broker, port):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client, topic):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        write_to_influxdb(str(msg.topic), msg.payload)

    client.subscribe(topic + "/#")
    client.on_message = on_message

def main():
    broker = config['mqtt']['broker']
    port = int(config['mqtt']['port'])
    topic = config['mqtt']['topic']

    client_id = "monitor"
    client = connect_mqtt(client_id, broker, port)
    subscribe(client, topic)
    client.loop_forever()
         

if __name__ == '__main__':
    main()