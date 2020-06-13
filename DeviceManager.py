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
    def __init__(self,smartBulbs,sensorNodes):
        self.smartBulbs = smartBulbs
        self.sensorNodes = sensorNodes

    def fetchBulbs(self):
        print(str(discover_bulbs()))

    def fetchAvailableDevices(self):
        self.fetchBulbs()