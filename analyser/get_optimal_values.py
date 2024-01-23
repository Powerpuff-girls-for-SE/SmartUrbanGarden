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
            

def get_optimal_value(garden_area, sensor):
    return int(config[garden_area][sensor])
    