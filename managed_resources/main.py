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

    broker = config['mqtt']['broker']
    port = int(config['mqtt']['port'])

    client_id = 'managed_resource'
    client = connect_mqtt(client_id, broker, port)

    # GardenArea creation
    areas = []

    area1 = GardenArea(areaName=config["Rose"]["area_name"],  light=config["Rose"]["light"], temperature=config["Rose"]["temperature"], humidity=config["Rose"]["humidity"], moisture=config["Rose"]["moisture"])
    areas.append(area1)
    area2 = GardenArea(areaName=config["Basil"]["area_name"],  light=config["Basil"]["light"], temperature=config["Basil"]["temperature"], humidity=config["Basil"]["humidity"], moisture=config["Basil"]["moisture"])
    areas.append(area2)
    area3 = GardenArea(areaName=config["Succulent"]["area_name"],  light=config["Succulent"]["light"], temperature=config["Succulent"]["temperature"], humidity=config["Succulent"]["humidity"], moisture=config["Succulent"]["moisture"])
    areas.append(area3)
    area4 = GardenArea(areaName=config["FernOasis"]["area_name"],  light=config["FernOasis"]["light"], temperature=config["FernOasis"]["temperature"], humidity=config["FernOasis"]["humidity"], moisture=config["FernOasis"]["moisture"])
    areas.append(area4)

    while True:
        for area in areas:
            area.publish_sensor_data(client=client)

        time.sleep(1)

if __name__ == "__main__":
    main()