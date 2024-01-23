import time
import paho.mqtt.client as mqtt

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

class MQTTSubscriber:
    def __init__(self, broker_address, topic):
        self.broker_address = broker_address
        self.topic = topic
        self.payload = None

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        # Subscribing to the topic when connected
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        print(f"Received message on topic {msg.topic}: {msg.payload}")
        # Save the payload
        self.payload = msg.payload.decode("utf-8")

    def subscribe_and_get_payload(self):
        # Create an MQTT client
        client = mqtt.Client()

        # Set up callbacks
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        # Connect to the MQTT broker
        client.connect(self.broker_address, 1883, 60)

        # Loop in the background to handle incoming messages
        client.loop_start()

        # Wait for a moment to ensure the connection is established
        time.sleep(2)

        try:
            # Keep the script running until a message is received
            while self.payload is None:
                time.sleep(1)

            return self.payload

        finally:
            # Disconnect from the MQTT broker
            client.loop_stop()
            client.disconnect()

optimal_value_mappings = {
    "Rose": {
        "light": 2000,
        "temperature": 20,
        "humidity": 60,
        "moisture": 50
    },
    "Basil": {
        "light": 5000,
        "temperature": 25,
        "humidity": 70,
        "moisture": 70
    },
    "Succulent": {
        "light": 10000,
        "temperature": 25,
        "humidity": 40,
        "moisture": 30
    },
    "FernOasis": {
        "light": 1500,
        "temperature": 22,
        "humidity": 75,
        "moisture": 60
    },
}

def get_optimal_value(garden_area, sensor):
    # broker_address = config["mqtt"]["broker"]
    # topic = f"garden/{garden_area}/optimal_{sensor}"
    # subscriber = MQTTSubscriber(broker_address, topic)
    # payload = subscriber.subscribe_and_get_payload()

    # return payload
    return optimal_value_mappings[garden_area][sensor]
    