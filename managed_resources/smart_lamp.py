import paho.mqtt.client as mqtt

class SmartLamp:
    def __init__(self, garden, client: mqtt.Client):
        self.garden = garden
        self.client = client
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.connect("localhost", 1883, 60)
        self.client.subscribe("garden/lamp")

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

    def on_disconnect(self, client, userdata, rc):
        print("Disconnected with result code " + str(rc))

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        if msg.payload == b"ON":
            print("Lamp is on")
        elif msg.payload == b"OFF":
            print("Lamp is off")
        else:
            print("Unknown command")

    def run(self):
        self.client.loop_forever()