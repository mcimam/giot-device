from machine import Pin, ADC
from dht import DHT11

class DHT:
    def __init__(self, PIN) -> None:
        self.sensor = DHT11(Pin(PIN, Pin.IN))
        print("DHT11 - {}".format(PIN))

    def get(self) -> dict:
        result = {
            "temp": 0,
            "hum": 0
        }

        try:
            self.sensor.measure()
            result["temp"] = self.sensor.temperature()
            result["hum"] = self.sensor.humidity()
            
        except OSError as e:
            print('DHT_ERROR : ', end='')
            print(e)
            result["err_dht"] = e

        finally:
            return result

class TDS:
    def __init__(self, PIN) -> None:
        self.sensor = ADC(Pin(PIN, Pin.IN))
        self.sensor.atten(ADC.ATTN_11DB)
        print("TDS - {}".format(PIN))

    
    def get(self) -> None:
        result = {
            "tds": 0
        }

        try:
            result["tds"] = self.sensor.read_uv()
        except OSError as e:
            print('TDS_ERROR : ', end='')
            print(e)
            result["err_tds"] = e
        finally:
            return result


class Water:
    def __init__(self, PIN) -> None:
        self.sensor = ADC(Pin(PIN, Pin.IN))
        self.sensor.atten(ADC.ATTN_11DB)
        print("Water - {}".format(PIN))

    def get(self) -> None:
        result = {
            "water": 0
        }

        try:
            result["water"] = self.sensor.read_uv()
        except OSError as e:
            print('WATER_ERROR : ', end='')
            print(e)
            result["err_water"] = e
        finally:
            return result

class Relay:
    def __init__(self, PIN) -> None:
        self.relay = Pin(PIN, Pin.OUT)
        self.state = 1
        self.relay.value(self.state)
        print("Relay - {}".format(PIN))

    
    def set(self, state) -> None:
        self.state = state
        self.relay.value(self.state)

    def get(self) -> int:
        return self.state

    def get_dict(self) -> dict:
        return {
            "relay": self.state
        }