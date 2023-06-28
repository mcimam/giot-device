# Garam IOT Device

This device is designed to automate sea salt production. 

Sea salt is made using several tunnels. Seawater is channeled into the tunnels. Each tunnel serves as a place for the evaporation of seawater. When the combination of salt and water levels reaches a certain amount, the seawater is channeled to the next tunnel.



## Device Description

![Device Anim](device_anim.png)

| Component           | Description                   |  Port |
|-------------------  |:------------------------------|------:|
| ESP32               | Microcontroller               | -     |
| Water Level Sensor  | Random Water Level Sensor     |    35 |
| DHT 11              | Temperature - Humidity Sensor |    26 |
| Relay               | 1ch Relay                     |    27 |
| Salinity Sensor     | TDS Sensor                    |    34 |


## Device Algorithm

``` 
tds_param   = value to open gate
water_param = value to close gate

cur_temp = measurement from temperature device
cur_hum = measurement from humidity device
cur_tds = measurement from salinity sensor
cur_water = measurement from water level sensor

if(cur_tds <= tds_param and cur_water <= water_param): 

    

If  

```

## How To Use
### Flash ESP 32 with micropython firmware
1. Download esp32 firmware from [here](https://micropython.org/download/esp32/)

2. Install esptool 
``` bash
pip install esptool setuptools
```

3. Flash firmware
Port can be find in /dev (ubuntu) or device manager (windows)
Note: For linux user, if error could not open <port>, the port doesn't exist, please run sudo chmod a+rw /dev/ttyUSB0

``` bash
python -m esptool --chip esp32 erase_flash
python -m esptool --chip esp32 --port <serial_port> write_flash -z 0x1000 <esp32-X.bin>
```


2. Edit Config 


3. Compile and Insert Main.py to esp32