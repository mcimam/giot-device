# main.py -- BAsically lazy way to emulate
# from machine import Pin, reset
import sys
sys.path.append('/home/mcimam/PersonalProject/KR/device/giot-device/src')
from time import sleep

from rpc_controller import OdooAPI
from sensor_sandbox import DHT, TDS, Water, Relay

from config import DHT_PIN, TDS_PIN, WATER_PIN, RELAY_PIN, TDS_PARAM, WATER_PARAM, OPEN_TIME, SLEEP_TIME, DELAY

# Set sandbox consonant
sleep_time = 1
l =0
limit = 10


# Set Device Sensor
d_dht   = DHT(DHT_PIN)
d_water = Water(WATER_PIN)
d_tds   = TDS(TDS_PIN)
d_relay = Relay(RELAY_PIN)

device_state = {
    'relay': 1,
    'dht' : 1,
    'water': 1,
    'tds': 1,
}

device_config = {
    'realy': 1,
    'delay' : DELAY,
    'tds_param': TDS_PARAM,
    'water_param': WATER_PARAM,
    'open_time': OPEN_TIME
}

opi = OdooAPI()

print("start simulation")
while True:
    if(l >= limit):
        break
    l = l+1
    sleep(1)


    # Get Data
    dvc = {}
    if(device_state['dht'] == 1):
        dvc.update(d_dht.get())
    if(device_state['water'] == 1):
        dvc.update(d_water.get())
    if(device_state['tds'] == 1):
        dvc.update(d_tds.get())
    if(device_state['relay'] == 1):
        dvc.update(d_relay.get_dict())
    
    # generate log file
    opi.report_log(dvc)
    
    # auto switch logic
    tds_value = dvc['tds']
    water_value = dvc['water']
    
    if(tds_value <= TDS_PARAM and water_value <= WATER_PARAM):
        # d_relay.set(0) #set relay on
        sleep(OPEN_TIME)
        # d_relay.set(1) #set relay off
    
    # process ,essage
    cmds = opi.get_cmd()
    for cmd in cmds:
        if cmd["method"] == 'ping':
            opi.rtr_cmd(cmd["id"], {'result': 'ping success'})
        elif cmd["method"] == 'reset':
            # reset()
            opi.rtr_cmd(cmd["id"], {'result': 'reset device'})
        elif cmd["method"] == 'set':
            pass
        
    sleep(sleep_time)
    print('---')
    print(dvc)
    print('=====')
    
    
print("stop simulation")