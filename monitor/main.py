import influxdb_client
import paho.mqtt.client as mqtt
from influxdb_client.client.write_api import SYNCHRONOUS

class Database:
    @staticmethod
    def write_to_database(topic : str, value: int):
        #influxdb connection
        bucket = "smartGarden"
        org = "powerpuffGirls"
        token = "smartGardenInfluxDBtoken"
        url = "http://173.20.0.102:8086/"
        client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
        write_api = client.write_api(write_options=SYNCHRONOUS)

        #data formatting and storing
        topic = topic.split("/")
        measurement = topic[0]
        field = topic[1]
        p = influxdb_client.Point(measurement).field(field, int(value))
        write_api.write(bucket=bucket, org=org, record=p)

def on_connect(client, userdata, flags, rc):
    client.subscribe("indoor/#")

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print(str(msg.topic + " -> " + payload))
    Database.write_to_database(str(msg.topic), payload)

if __name__ == '__main__':
    client = mqtt.Client(client_id="MONITOR", reconnect_on_failure=True)
    #client.connect("localhost", 1883)
    client.connect("173.20.0.100", 1883)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()

