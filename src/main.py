# main.py -- put your code here!
from machine import Pin
from time import sleep

from controller.wifi_controller import connectWifi
from controller.mqtt_contoller import MQTTMessage
from controller.sensor_controller import DHT, TDS, Water, Relay

from config import DHT_PIN, TDS_PIN, WATER_PIN, RELAY_PIN, TDS_PARAM, WATER_PARAM, OPEN_TIME, SLEEP_TIME

# BUILD IN LED CONTROLLER
LED_2 = Pin(2, Pin.OUT)

def dimm(tick=1):
    for i in range(0,tick):
        LED_2.value(1)
        sleep(1)
        LED_2.value(0)

# Set Dynamic Parameter
sleep_time = SLEEP_TIME

dimm()
wifi = connectWifi()
dimm(2)

# Set Device Sensor
d_dht   = DHT(DHT_PIN)
d_water = Water(WATER_PIN)
d_tds   = TDS(TDS_PIN)
d_relay = Relay(RELAY_PIN)

mqttm = MQTTMessage(wifi)

device = mqttm.getDevice()
config = mqttm.getConfig()

while True:
    LED_2.value(1)
    sleep(1)

    # Get MQTT
    mqttm.checkMsg()

    # Get Data
    dvc = {}
    if(device['dht'] == 1):
        dvc.update(d_dht.get())
    if(device['water'] == 1):
        dvc.update(d_water.get())
    if(device['tds'] == 1):
        dvc.update(d_tds.get())
    if(device['relay'] == 1):
        dvc.update(d_relay.get_dict())
    mqttm.generateLoopMsg(dvc)

    # auto switch logic
    tds_value = dvc['tds']
    water_value = dvc['water']
    
    if(tds_value <= TDS_PARAM and water_value <= WATER_PARAM):
        d_relay.set(0) #set relay on
        sleep(OPEN_TIME)
        d_relay.set(1) #set relay off

    # Send Data
    LED_2.value(0)
    sleep(sleep_time)