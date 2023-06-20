# Package For Creating and Handling MQTT Message
from ubinascii import hexlify
from umqtt.simple import MQTTClient
from config import MQTT_URL, MQTT_PORT, MQTT_TOPIC, MQTT_USER, MQTT_PASSWORD, DEVICE_PASSWORD, DELAY, TDS_PARAM, WATER_PARAM, OPEN_TIME
from random import randint
import ujson
import machine


class MQTTMessage:
    def __init__(self, STA_NET):
        self.msg = {
            'device': {},
            'mac'   : hexlify(STA_NET.config('mac')).decode()
        }

        # Activate Device 
        self.device = {
            'relay': 1,
            'dht' : 0,
            'water': 1,
            'tds': 1,
        }

        self.config = {
            'realy': 1,
            'delay' : DELAY,
            'tds_param': TDS_PARAM,
            'water_param': WATER_PARAM,
            'open_time': OPEN_TIME
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
        
    def handleCMD(self, topic, pl):
        dt = ujson.loads(pl)

        if('cmd' not in dt):
            return
        
        try:
            result = {
                'id': dt.get('id', None)
            }
            print(dt)

            if('config' in dt):
                self.setConfig(self.config.update(dt['config']))
                result.update({'result': self.config})
                pass
            
            if('device' in dt):
                self.setConfig(self.device.update(dt['device']))
                result.update({'result': self.device})
                pass

            # 
            if('method' in dt):
                # auth with builtin pass
                if (dt['params']['pass'] != DEVICE_PASSWORD):
                    self.sendMsg(result.update({'error': 'Wrong Password'}))
                    return

                if (dt['method'] == 'exec'):
                    result = eval(dt['params']['cmd'])
                    self.sendMsg(result.update({'result': result}))
                    return
                    
                if (dt['method'] == 'reset'):
                    self.sendMsg(result.update({'result': 'reset device'}))
                    machine.reset()    
                    return                

                pass

            self.sendMsg({
                'id': dt.get('id', None),
                'result': result,
            })
        
        except OSError as e:
            print(e)
            self.sendMsg({
                'id': dt.get('id', None),
                'error': e
                })
        
        except:
            print("CMD_Error: Unknown Error")
            self.sendMsg({
                'id': dt.get('id', None),
                'error': 'unknown error'
                })

    def checkMsg(self):
        self.client.check_msg()
            
    def sendMsg(self, data):
        self.client.publish(self.topic, ujson.dumps(data))

    def generateLoopMsg(self, data, param={}):
        # Generate Loop Message
        msg = self.msg
        msg['id'] = randint(1,999)
        msg['device'] = data
        msg['config'] = param
        self.client.publish(self.topic, ujson.dumps(data))

    def getConfig(self):
        return self.config
    
    def setConfig(self, config):
        self.config.update(config)

    def getDevice(self):
        return self.device
    
    def setDevice(self, device):
        self.device.update(device)