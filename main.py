import time
import mysql.connector
import DatabaseManager
import SmartBulbManager
import DeviceManager
# Init Database

database = DatabaseManager.DatabaseConnector('localhost','smarthome','root','mateus12345')
database.connect()
database.createDataModel()

# Discover available devices

deviceManager = DeviceManager.DeviceManager()
deviceManager.fetchAvailableDevices()


# Create Bulb
#print('aqui')
#bulb = SmartBulbManager.SmartBulb('Luz do Quarto','192.168.15.14')
#bulb.turnOff()
database.disconnect()
