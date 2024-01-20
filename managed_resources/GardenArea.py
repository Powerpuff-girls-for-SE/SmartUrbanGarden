import random
from random import randint
from paho.mqtt.client import Client
import Thermostat
import SmartLamp
import Humidifier
import WaterPump


class GardenArea:

    areaName = "" # Plant Name
    light = 0     # Lux
    temperature = 30    # Celcius
    humidity = 0    # Percentage
    moisture = 1    # Percentage

    def __init__(self, areaName: str, light: int, temperature: int, humidity: int, moisture: int):
        self.areaName = areaName
        self.light = light
        self.temperature = temperature
        self.humidity = humidity
        self.moisture = moisture
        self.actuators = [Thermostat.Thermostat(self),
                          SmartLamp.SmartLamp(self),
                          Humidifier.Humidifier(self),
                          WaterPump.WaterPump(self)]


    def simulate(self, client: Client):
        rand = random.randint(0,9)
        if rand == 0:
             self.light = self.light + randint(-1, 1)
             self.temperature = self.temperature + randint(-1, 1)
             self.humidity = self.humidity + randint(-1, 1)
             self.moisture = randint(0,1)

        client.publish(f"garden/{self.areaName}/light", self.light)
        client.publish(f"garden/{self.areaName}/temperature", self.temperature)
        client.publish(f"garden/{self.areaName}/humidity", self.humidity)
        client.publish(f"garden/{self.areaName}/moisture", self.moisture)

        print(f'Publishing simulated data for Garden Area {self.areaName}')