import time
import paho.mqtt.client as mqtt_client
import configparser
from Garden import GardenArea

def connect_mqtt(client_id, broker, port):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, topic, msg):
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

def publish_area_optimal_values(client, area_name, optimal_light, optimal_temperature, optimal_humidity, optimal_moisture):
    publish(client, f"garden/{area_name}/optimal_light", optimal_light)
    publish(client, f"garden/{area_name}/optimal_temperature", optimal_temperature)
    publish(client, f"garden/{area_name}/optimal_humidity", optimal_humidity)
    publish(client, f"garden/{area_name}/optimal_moisture", optimal_moisture)

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    broker = '172.100.0.13'
    port = 1883
    client_id = 'managed_resource'

    client = connect_mqtt(client_id, broker, port)

    # GardenArea creation
    areas = []

    area1 = GardenArea(areaName="Rose",  light=290, temperature=20, humidity=60, moisture=50)
    areas.append(area1)
    publish_area_optimal_values(client, "Rose", 290, 20, 60, 50)
    area2 = GardenArea(areaName="Basil", light=500, temperature=25, humidity=70, moisture=70)
    areas.append(area2)
    publish_area_optimal_values(client, "Basil", 500, 25, 70, 70)
    area3 = GardenArea(areaName="Succulent",  light=800, temperature=25, humidity=40, moisture=30)
    areas.append(area3)
    publish_area_optimal_values(client, "Succulent", 800, 25, 40, 30)
    area4 = GardenArea(areaName="FernOasis", light=300, temperature=22, humidity=75, moisture=60)
    areas.append(area4)
    publish_area_optimal_values(client, "FernOasis", 300, 22, 75, 60)

    while True:
        for area in areas:
            area.publish_sensor_data(client=client)

        time.sleep(1)

if __name__ == "__main__":
    main()