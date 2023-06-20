import network
from config import WIFI_ID, WIFI_PASSWORD
from time import sleep

def connectWifi():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)

    if not sta_if.isconnected():
        sta_if.connect(WIFI_ID, WIFI_PASSWORD)
        print("Connecting to {}".format(WIFI_ID), end="")

    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.5)

    print("Connected to {}".format(WIFI_ID))
    return sta_if
