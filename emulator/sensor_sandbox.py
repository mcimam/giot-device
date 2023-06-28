import random

class DHT:
    def __init__(self, PIN) -> None:
        print("DHT11 - {}".format(PIN))

    def get(self) -> dict:
        result = {
            "temp": 0,
            "hum": 0
        }

        try:
            result["temp"] = random.randrange(10, 30)
            result["hum"] = random.randrange(15, 30)
            
        except OSError as e:
            print('DHT_ERROR : ', end='')
            print(e)
            result["err_dht"] = e

        finally:
            return result

class TDS:
    def __init__(self, PIN) -> None:
        print("TDS - {}".format(PIN))

    
    def get(self) -> None:
        result = {
            "tds": 0
        }

        try:
            result["tds"] = random.randrange(-10000, 3000)
        except OSError as e:
            print('TDS_ERROR : ', end='')
            print(e)
            result["err_tds"] = e
        finally:
            return result


class Water:
    def __init__(self, PIN) -> None:
        print("Water - {}".format(PIN))

    def get(self) -> None:
        result = {
            "water": 0
        }

        try:
            result["water"] = random.randrange(0, 100)
        except OSError as e:
            print('WATER_ERROR : ', end='')
            print(e)
            result["err_water"] = e
        finally:
            return result

class Relay:
    def __init__(self, PIN) -> None:
        self.state = 1
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