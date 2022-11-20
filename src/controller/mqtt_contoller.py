# Package For Creating and Handling MQTT Message
from ubinascii import hexlify
from umqtt.simple import MQTTClient
from config import MQTT_URL, MQTT_PORT, MQTT_TOPIC, MQTT_USER, MQTT_PASSWORD
import ujson

class MQTTMessage:
    def __init__(self, STA_NET):
        self.msg = {
            'device': {},
            'mac'   : hexlify(STA_NET.config('mac')).decode()
        }

        try:
            
            print("Connecting to MQTT server... ", end="")           
            self.client = MQTTClient(self.msg['mac'],MQTT_URL, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD)
            self.client.connect()

            self.topic = MQTT_TOPIC + self.msg["mac"]
            self.client.publish(self.topic, ujson.dumps(self.msg) , retain=False, qos=0)

            # Subscribing to MQTT
            self.client.set_callback(self.handleCMD)
            self.client.subscribe(self.topic)

            print("Connected")
            print("{} | {}".format(MQTT_URL, self.topic))           


        except OSError as e:
            print(e)
        
    def handleCMD(self):
        pass

    def generateLoopMsg(self, data):
        # Generate Loop Message
        self.client.publish(self.topic, ujson.dumps(data))
