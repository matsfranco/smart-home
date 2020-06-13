###############################################################################
# Name: DatabaseManager
#
#
##############################################################################
import time
from datetime import date,datetime,timedelta
import mysql.connector
from mysql.connector import errorcode

class DatabaseConnector :

  def __init__(self,host,schema,user,password):
    self.host = host
    self.schema = schema
    self.user = user 
    self.password = password
    print('>> DatabaseConnector.init() - New DatabaseConnector defined: '+self.host+' on schema '+self.schema+' as '+self.user)

  def connect(self) :
    self.mydb = mysql.connector.connect(host=self.host,user=self.user,password=self.password)
    self.cursor = self.mydb.cursor()
    print('>> DatabaseConnector - Connection Opened - '+str(self.mydb))

  def disconnect(self) :
    self.mydb.commit()
    self.cursor.close()
    self.mydb.close()
    print('>> DatabaseConnector - Connection Closed')
 
  def createSchema(self):
    query = "CREATE SCHEMA IF NOT EXISTS %s" %self.schema
    self.cursor.execute(query)
    print('>> DatabaseConnector - Schema created')

  def useSchema(self):
    query = "USE %s" %self.schema
    self.cursor.execute(query)
    print('>> DatabaseConnector - Use '+self.schema+' schema')

  def createTables(self):
    query = "CREATE TABLE IF NOT EXISTS Bulb (CreatedDate DATETIME, LastModifiedDate DATETIME , Name VARCHAR(100), IP VARCHAR(15) NOT NULL, Model VARCHAR(20), Effect VARCHAR(10), Duration INT, Auto_On BOOLEAN, Power_Mode INTEGER, CONSTRAINT Id PRIMARY KEY(IP))"
    self.cursor.execute(query)

  def createDataModel(self):
    self.createSchema()
    self.useSchema()
    self.createTables()

  def getBulb(self,IP):
    query = ("SELECT IP FROM Bulb WHERE IP = '%s'" % IP)
    self.cursor.execute(query)
    bulbIP = list(self.cursor.fetchall())
    return bulbIP

  def newBulb(self,IP,Name,Model,Effect,Duration,Auto_On,Power_Mode) :
    bulbIP = self.getBulb(IP)
    if not bulbIP:
      query = "INSERT INTO Bulb(CreatedDate,LastModifiedDate,IP,Name,Model,Effect,Duration,Auto_On,Power_Mode) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      args = (datetime.now(),datetime.now(),IP,Name,Model,Effect,Duration,Auto_On,Power_Mode)
      self.cursor.execute(query,args)
      self.mydb.commit()
      print('>> DatabaseConnector - New Bulb Inserted. Name: '+Name+' IP: '+IP)
      return 'INSERTION SUCCEEDED'
    else:
      print('>> DatabaseConnector - Bulb already inserted')
      return 'INSERTION FAILED'

#database = DatabaseConnector('localhost','smarthome','root','mateus12345')
#database.connect()
#database.createDataModel()
#database.disconnect()