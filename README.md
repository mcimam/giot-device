# Garam IOT Device

Source Code For Garam IOT Device

## Device Description

| Component           | Description                   |  Port |
|-------------------  |:------------------------------|------:|
| ESP32               | Microcontroller               | -     |
| Water Level Sensor  | Random Water Level Sensor     |    35 |
| DHT 11              | Temperature - Humidity Sensor |    26 |
| Relay               | 1ch Relay                     |    27 |
| Salinity Sensor     | TDS Sensor                    |    34 |

## How To Use
### Flash ESP 32 with micropython firmware
1. Download esp32 firmware from [here](https://micropython.org/download/esp32/)

2. Install esptool 
``` bash
pip install esptool setuptools
```

3. Flash firmware
Port can be find in /dev (ubuntu) or device manager (windows)
``` bash
python -m esptool --chip esp32 erase_flash
python -m esptool --chip esp32 --port <serial_port> write_flash -z 0x1000 <esp32-X.bin>
```

2. Edit Config 


3. Compile and Insert Main.py to esp32