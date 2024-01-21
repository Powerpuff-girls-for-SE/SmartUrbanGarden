import random
import pandas as pd
from random import randint
from paho.mqtt.client import Client

from Actuators import SmartBulb, Thermostat, WaterPump, Humidifier

class GardenArea:

    areaName = "" # name of the garden area
    light = 0     # measured in lux
    temperature = 30    # measured in celsius
    humidity = 0    # measured in percentage
    moisture = 1    # measured in percentage

    def __init__(self, areaName: str, light: int, temperature: int, humidity: int, moisture: int):
        self.areaName = areaName
        self.optimal_light_value = light
        self.optimal_temperature = temperature
        self.optimal_humidity = humidity
        self.optimal_moisture = moisture
        self.light = light
        self.temperature = temperature
        self.humidity = humidity
        self.moisture = moisture
        self.actuators = [Thermostat(self),
                          SmartBulb(self),
                          Humidifier(self),
                          WaterPump(self)]


    def publish_sensor_data(self, client: Client):
        df = pd.read_csv("urban_garden_sensor_data.csv")
        selected_row = df.sample()

        self.light = selected_row['light_intensity'].values[0]
        self.temperature = selected_row['temperature'].values[0]
        self.humidity = selected_row['humidity'].values[0]
        self.moisture = selected_row['soil_moisture'].values[0]

        client.publish(f"garden/{self.areaName}/light", self.light)
        client.publish(f"garden/{self.areaName}/temperature", self.temperature)
        client.publish(f"garden/{self.areaName}/humidity", self.humidity)
        client.publish(f"garden/{self.areaName}/moisture", self.moisture)

        print(f'Publishing generated data for Garden Area {self.areaName}')