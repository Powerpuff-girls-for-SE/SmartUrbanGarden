import time
import paho.mqtt.client as mqtt
import tenacity
from GardenArea import GardenArea

def main():
    # MQTT client creation
    client = mqtt.Client("ManagedResource", reconnect_on_failure=True)
    #client.connect("localhost")
    client.connect("173.20.0.100")

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
            GardenArea.publish_sensor_data(client=client)

        time.sleep(1)

if __name__ == "__main__":
    main()