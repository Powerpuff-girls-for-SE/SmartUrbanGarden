import time
import paho.mqtt.client as mqtt
import tenacity
import configparser
from managed_resources.GardenArea import GardenArea

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    # MQTT client creation
    mqtt_client = mqtt.Client(client_id="managed_resources")
    mqtt_client.connect(config['mqtt']['broker'], int(config['mqtt']['port']))

    # GardenArea creation
    areas = []

    area1 = GardenArea(areaName="Rose",  light=2000, temperature=20, humidity=60, moisture=50)
    areas.append(area1)
    area2 = GardenArea(areaName="Basil", light=5000, temperature=25, humidity=70, moisture=70)
    areas.append(area2)
    area3 = GardenArea(areaName="Succulent",  light=10000, temperature=25, humidity=40, moisture=30)
    areas.append(area3)
    area4 = GardenArea(areaName="FernOasis", light=1500, temperature=22, humidity=75, moisture=60)
    areas.append(area4)


    while True:
        for GardenArea in areas:
            GardenArea.publish_sensor_data(client=mqtt_client)

        time.sleep(1)

if __name__ == "__main__":
    main()