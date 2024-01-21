import time
import paho.mqtt.client as mqtt
from paho.mqtt.client import Client
import configparser
from GardenArea import GardenArea

def publish_area_optimal_values(client, area_name, optimal_light, optimal_temperature, optimal_humidity, optimal_moisture):
    client.publish(f"garden/{area_name}/optimal_light", optimal_light)
    client.publish(f"garden/{area_name}/temperature", optimal_temperature)
    client.publish(f"garden/{area_name}/humidity", optimal_humidity)
    client.publish(f"garden/{area_name}/moisture", optimal_moisture)

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    # MQTT client creation
    mqtt_client = mqtt.Client(client_id="managed_resources", reconnect_on_failure=True)
    mqtt_client.connect(config['mqtt']['broker'])

    # GardenArea creation
    areas = []

    area1 = GardenArea(areaName="Rose",  light=2000, temperature=20, humidity=60, moisture=50)
    areas.append(area1)
    publish_area_optimal_values(mqtt_client, "Rose", 2000, 20, 60, 50)
    area2 = GardenArea(areaName="Basil", light=5000, temperature=25, humidity=70, moisture=70)
    areas.append(area2)
    publish_area_optimal_values(mqtt_client, "Basil", 5000, 25, 70, 70)
    area3 = GardenArea(areaName="Succulent",  light=10000, temperature=25, humidity=40, moisture=30)
    areas.append(area3)
    publish_area_optimal_values(mqtt_client, "Succulent", 10000, 25, 40, 30)
    area4 = GardenArea(areaName="FernOasis", light=1500, temperature=22, humidity=75, moisture=60)
    areas.append(area4)
    publish_area_optimal_values(mqtt_client, "FernOasis", 1500, 22, 75, 60)

    while True:
        for area in areas:
            area.publish_sensor_data(client=mqtt_client)

        time.sleep(1)

if __name__ == "__main__":
    main()