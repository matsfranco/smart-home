from yeelight import discover_bulbs
from yeelight import Bulb
import time
import mysql.connector

import DatabaseManagement

database = DatabaseManagement.DatabaseConnector('localhost','smarthome','root','mateus12345')
database.connect()
database.createDataModel()
database.disconnect()