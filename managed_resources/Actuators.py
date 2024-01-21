from threading import Thread
from tenacity import retry
import paho.mqtt.client as mqtt

class Actuator:
    def __init__(self, gardenArea, actuatorType):
        self.gardenArea = gardenArea
        self.client = mqtt.Client(client_id=f"{actuatorType}_{gardenArea.areaName}")
        self.subscription_topic = actuatorType
        thread = Thread(target=self.initialize_mqtt)
        thread.start()

    def initialize_mqtt(self):
        self.client.connect("173.20.0.100", 1883)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.in_disconnect = self.on_disconnect
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        self.client.subscribe(f"{self.subscription_topic}/#")

    def on_disconnect(self, client, userdata, rc):
        print("Disconnected with result code " + str(rc))


class SmartBulb(Actuator):
    def __init__(self, gardenArea):
        super().__init__(gardenArea, "smartBulb")
        self.gardenArea = gardenArea
        self.light_level = "off"
        self.light_levels_mappings = {
            "off": 0,
            "low": 200,
            "high": 1000
        }

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode("utf-8")
        topic = msg.topic
        topic_split = topic.split('/')
        garden_area = topic_split[1]
        light_level = topic_split[2]
        print(msg.topic + " " + str(msg.payload))
        if garden_area == self.areaName:
            self.set_light_level(light_level)
            self.gardenArea.light = self.light_levels_mappings[light_level]

    def set_light_level(self, light_level):
        self.light_level = light_level

class Thermostat(Actuator):
    def __init__(self, gardenArea):
        super().__init__(gardenArea, "thermostat")
        self.thermostat_state = "off"

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode("utf-8")
        topic = msg.topic
        topic_split = topic.split('/')
        garden_area = topic_split[1]
        action = topic_split[2]
        print(msg.topic + " " + str(msg.payload))
        if garden_area == self.areaName:
            if action == "on":
                self.turn_thermostat_on()
                print(f"Thermostat in {garden_area} turned on")
            elif action == "off":
                self.turn_thermostat_off()
                print(f"Thermostat in {garden_area} turned off")

    def turn_thermostat_on(self):
        self.thermostat_state = "on"
        self.gardenArea.temperature = self.gardenArea.optimal_temperature

    def turn_thermostat_off(self):
        print("Thermostat turned off so temperature value remains unaffected")

class WaterPump(Actuator):
    def __init__(self, gardenArea):
        super().__init__(gardenArea, "water_pump")
        self.water_pump_state = "off"

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode("utf-8")
        topic = msg.topic
        topic_split = topic.split('/')
        garden_area = topic_split[1]
        action = topic_split[2]
        print(msg.topic + " " + str(msg.payload))
        if garden_area == self.areaName:
            if action == "on":
                self.turn_water_pump_on()
                print(f"Water pump in {garden_area} turned on")
            elif action == "off":
                self.turn_water_pump_off()
                print(f"Water pump in {garden_area} turned off")

    def turn_water_pump_on(self):
        self.water_pump_state = "on"
        self.gardenArea.moisture = self.gardenArea.optimal_moisture

    def turn_water_pump_off(self):
        self.water_pump_state = "off"
        print("Water pump turned off so water level value remains unaffected")
        
class Humidifier(Actuator):
    def __init__(self, gardenArea):
        super().__init__(gardenArea, "humidifier")
        self.humidifier_state = "off"
        self.light_levels_mappings = {
            "off": 0,
            "low": 20,
            "high": 90
        }

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode("utf-8")
        topic = msg.topic
        topic_split = topic.split('/')
        garden_area = topic_split[1]
        humidifier_level = topic_split[2]
        print(msg.topic + " " + str(msg.payload))
        if garden_area == self.areaName:
            self.set_humidifier_level()
            self.gardenArea.humidity = self.light_levels_mappings[humidifier_level]
  
    def set_humidifier_level(self, humidifier_level):
        self.humidifier_level = humidifier_level
