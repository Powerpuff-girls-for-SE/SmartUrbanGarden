import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self,client_id):
        self.client = mqtt.Client(client_id = client_id, reconnect_on_failure=True)
        self.client.on_publish = lambda client, userdata, mid: print("PUBLISH: ", mid)
        self.client.connect("173.20.0.100")
        #self.client.connect("localhost")

    def on_connect(client, userdata, flags, rc):
        print('Executor connected to MQTT')

    def publish(self, topic, msg):
        self.client.publish(topic, msg)