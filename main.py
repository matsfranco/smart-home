import time
import mysql.connector
import DatabaseManager
import SmartBulbManager
import DeviceManager
# Init Database

database = DatabaseManager.DatabaseConnector()
database.connect()
database.createDataModel()
database.disconnect()

# Discover available devices

deviceManager = DeviceManager.DeviceManager()
deviceManager.fetchAvailableDevices()

# Create Bulb
#print('aqui')
#bulb = SmartBulbManager.SmartBulb('Luz do Quarto','192.168.15.14')
#bulb.turnOff()

