############################################################################
# Name: DeviceManager Class
# Description: 
#   Class to implement Device Management for Smart Bulbs, sensor nodes and 
#   another kind of connected device.
# Module Dependencies: 
#   - YeeLight
# Created by: Mateus Franco @ 13/06/2020
# Change Log:
############################################################################
from yeelight import discover_bulbs
from yeelight import Bulb
from yeelight import LightType
import SmartBulbManager

class DeviceManager:
    def __init__(self):
        print('built')
        self.smartBulbs = []
        self.sensorNodes = []

    def fetchBulbs(self):
        for bulb in discover_bulbs():
            ip = bulb.get('ip')
            newBulb = SmartBulbManager.SmartBulb(ip)
            print(str(newBulb))

    def fetchAvailableDevices(self):
        self.fetchBulbs()