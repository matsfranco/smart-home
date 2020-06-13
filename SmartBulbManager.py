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

# Default erro messages
OUT_OF_BOUNDS = 'OUT_OFF_BOUNDS ERROR'

class SmartBulb:
    
    def __init__(self,ip):
        #self.bright = bright
        #self.color_mode =color_mode
        #self.ct = ct
        #self.fw_ver = fw_ver
        #self.hue = hue 
        #self.id = hue 
        #self.model = model
        #self.power = power
        #self.rgb = rgb
        #self.sat = sat
        #self.support = support
        #self.port = port
        
        self.bulb = Bulb(ip)
        capabilities = self.bulb.get_capabilities()
        self.ip = ip
        self.port = capabilities.get('port')
        self.name = capabilities.get('name')
        self.bright = capabilities.get('bright')
        self.color_mode = capabilities.get('color_mode')
        self.ct = capabilities.get('ct')
        self.fw_ver = capabilities.get('fw_ver')
        self.hue = capabilities.get('hue')
        self.model = capabilities.get('model')
        self.power = capabilities.get('power')
        self.rgb = capabilities.get('rgb')
        self.sat = capabilities.get('sat')
        self.support = capabilities.get('support')
        print('Name: '+self.name)
        print('IP: '+self.ip)

    def turnOn(self):
        self.bulb.turn_on()
        return self.name+' turned ON'

    def turnOff(self):
        self.bulb.turn_off()
        return self.name+' turned OFF'
    
    def setBrightness(self,brightness):
        if brightness >= 0 & brightness <=100 :
            self.bulb.set_brightness(brightness,light_type=LightType.Ambient)
            return 'Brightness '+self.name+'set: '+str(brightness)+' %'
        else:
            return OUT_OF_BOUNDS

    def setColorTemperature(self, temperature):
        if temperature >= 1700 & temperature <=6500 :
            self.bulb.set_color_temp(temperature)
            return 'Temperature of '+self.name+'set: '+str(temperature)+' K'
        else:
            return OUT_OF_BOUNDS

    def setRGB(self,red,green,blue):
        self.bulb.set_rgb(red,green,blue)

    def setHSV(self,hue,saturation,value):
        self.bulb.set_rgb(hue,saturation,value)

    def getProperties(self):
        return self.bulb.get_properties()