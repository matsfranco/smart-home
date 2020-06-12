from yeelight import discover_bulbs
from yeelight import Bulb
import time
import mysql.connector

lastEnvironmentId = 0

class Environment:
    def __init__(self, name, description,homeId):
        self.id = lastEnvironmentId + 1
        self.name = name
        self.description = description
        self.homeId = homeId
    
    def printEnvironmentData(self):
        print('Name: '+self.name)
        print('Description: '+self.description)
        print('homeId: '+self.homeId)


bulbs = [] 
bulbsRaw = ''

def createBulbs():
    newBulb = Bulb('192.168.15.14')
    bulbs.append(newBulb)

def discoverBulbs():
    bulbsRaw = discover_bulbs()
    print(str(bulbsRaw))

def unpackBulbInfo(ip = '', port = '', capabilities = ''):
    newBulb = Bulb(ip)
    print(str(newBulb))


env1 = Environment('Quarto','Quarto','0')