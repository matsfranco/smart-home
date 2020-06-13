from yeelight import discover_bulbs
from yeelight import Bulb
import time
import mysql.connector

import DatabaseManager

# Init Database

database = DatabaseManager.DatabaseConnector('localhost','smarthome','root','mateus12345')
database.connect()
database.createDataModel()

#print(str(database.getBulb('192.168.15.14')))



print(database.newBulb('192.168.15.14','Luz do Quarto','Color','Smooth',100,True,0))


# Closes Database Connection

database.disconnect()
