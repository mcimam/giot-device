# main.py -- put your code here!
from machine import Pin
from time import sleep

from controller.wifi_controller import connectWifi
from controller.mqtt_contoller import MQTTMessage
from controller.sensor_controller import DHT, TDS, Water, Relay

from config import DHT_PIN, TDS_PIN, WATER_PIN, RELAY_PIN

LED_2 = Pin(2, Pin.OUT)

def dimm(tick=1):
    for i in range(0,tick):
        LED_2.value(1)
        sleep(1)
        LED_2.value(0)


dimm()
wifi = connectWifi()
dimm(2)

# Set Device Sensor
d_dht   = DHT(DHT_PIN)
d_water = Water(WATER_PIN)
d_tds   = TDS(TDS_PIN)
d_relay = Relay(RELAY_PIN)

mqttm = MQTTMessage(wifi)

while True:
    LED_2.value(1)
    sleep(1)

    # Get Data
    msg = {}
    msg.update(d_dht.get())
    msg.update(d_water.get())
    msg.update(d_tds.get())
    msg.update(d_relay.get_dict())
    mqttm.generateLoopMsg(msg)

    # Send Data
    LED_2.value(0)
    sleep(10)