############################################################################
# Name: Bulb Class
# Description: 
#   Class to implement Bulb and its methods to control RGB/HSV Color,
#   Temperature, Status and other smart bulb parameters
# Module Dependencies: 
#   - YeeLight Library
# Created by: Mateus Franco @ 13/06/2020
# Change Log:
############################################################################
from yeelight import discover_bulbs
from yeelight import Bulb
from yeelight import LightType
import DatabaseManager
# Default erro messages
OUT_OF_BOUNDS = 'OUT_OFF_BOUNDS ERROR'

class SmartBulb:
    
    def __init__(self,ip):
        self.bulb = Bulb(ip)
        capabilities = self.bulb.get_capabilities()
        self.IP = ip
        self.Port = capabilities.get('port')
        self.Name = capabilities.get('name')
        self.Bright = capabilities.get('bright')
        self.Color_Mode = capabilities.get('color_mode')
        self.CT = capabilities.get('ct')
        self.Fw_Ver = capabilities.get('fw_ver')
        self.HUE = capabilities.get('hue')
        self.Model = capabilities.get('model')
        self.Power = capabilities.get('power')
        self.RGB = capabilities.get('rgb')
        self.Sat = capabilities.get('sat')
        self.Support = capabilities.get('support')
        self.Effect = 'smooth'
        self.Duration = 1000
        self.Auto_On = False
        self.Power_Mode = LightType.Ambient

    def turnOn(self):
        self.bulb.turn_on()
        return self.Name+' turned ON'

    def turnOff(self):
        self.bulb.turn_off()
        return self.Name+' turned OFF'
    
    def setBrightness(self,brightness):
        if brightness >= 0 & brightness <=100 :
            self.bulb.set_brightness(brightness,light_type=LightType.Ambient)
            return 'Brightness '+self.Name+'set: '+str(self.Bright)+' %'
        else:
            return OUT_OF_BOUNDS

    def setColorTemperature(self, temperature):
        if temperature >= 1700 & temperature <=6500 :
            self.bulb.set_color_temp(temperature)
            return 'Temperature of '+self.Name+'set: '+str(self.CT)+' K'
        else:
            return OUT_OF_BOUNDS

    def setRGB(self,red,green,blue):
        self.bulb.set_rgb(red,green,blue)

    def setHSV(self,hue,saturation,value):
        self.bulb.set_rgb(hue,saturation,value)

    def getProperties(self):
        return self.bulb.get_properties()
