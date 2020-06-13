############################################################################
# Name: DatabaseConnector Class
# Description: 
#   Implements all database initial configuration and query operations for
#   for specific use cases
# Module Dependencies: 
#   - mysql.connector
#   - time
#   - datetime
# Created by: Mateus Franco @ 13/06/2020
# Change Log:
############################################################################
import time
from datetime import date,datetime,timedelta
import mysql.connector
from mysql.connector import errorcode

host = 'localhost'
schema = 'smarthome'
user = 'root'
password = 'mateus12345'

# Default erro messages
INSERT_SUCCESS = 'INSERTION SUCCEEDED!'
INSERT_FAILED = 'INSERTION FAILED...'
UPDATE_SUCCESS = 'UPDATE SUCCEEDED!'
UPDATE_FAILED = 'UPDATE FAILED...!'

class DatabaseConnector :

  def __init__(self):
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
 
  def commit(self):
    self.mydb.commit()

  def createSchema(self):
    query = "CREATE SCHEMA IF NOT EXISTS %s" %self.schema
    self.cursor.execute(query)
    print('>> DatabaseConnector - Schema created')

  def useSchema(self):
    query = "USE %s" %self.schema
    self.cursor.execute(query)
    print('>> DatabaseConnector - Use '+self.schema+' schema')

  def createTables(self):
    query = \
      "CREATE TABLE IF NOT EXISTS Bulb (\
      CreatedDate DATETIME, \
      LastModifiedDate DATETIME , \
      Name VARCHAR(100), \
      Model VARCHAR(20), \
      IP VARCHAR(15) NOT NULL, \
      Port VARCHAR(10), \
      Bright INT, \
      Color_Mode INT,\
      CT INT, \
      Fw_Ver VARCHAR(7), \
      HUE INT,\
      Power VARCHAR(10),\
      RGB VARCHAR(9),\
      Sat INT,\
      Support VARCHAR(255),\
      Effect VARCHAR(10), \
      Duration INT, \
      Auto_On BOOLEAN, \
      Power_Mode VARCHAR(25), \
      CONSTRAINT Id PRIMARY KEY(IP)\
      )"
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

  def newBulb(self,newBulb):
    bulbIP = self.getBulb(newBulb.IP)
    if not bulbIP:
      now = (datetime.now() + timedelta(hours=+3))
      nowFormated = now.strftime('%Y-%m-%d %H:%M:%S')
      query = ("INSERT INTO Bulb (CreatedDate,LastModifiedDate,Name,Model,IP,Port,Bright,Color_Mode,CT,Fw_Ver,HUE,Power,RGB,Sat,Support,Effect,Duration,Auto_On,Power_Mode)\
              VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
      args = (nowFormated,nowFormated,newBulb.Name,newBulb.Model,newBulb.IP,newBulb.Port,newBulb.Bright,newBulb.Color_Mode,\
      newBulb.CT,newBulb.Fw_Ver,newBulb.HUE,newBulb.Power,newBulb.RGB,newBulb.Sat,newBulb.Support,newBulb.Effect,newBulb.Duration,\
      newBulb.Auto_On,str(newBulb.Power_Mode))
      self.cursor.execute(query,args)
      print('>> DatabaseConnector - New Bulb Inserted. Name: '+newBulb.Name+' IP: '+newBulb.IP)
      return INSERT_SUCCESS
    else:
      print('>> DatabaseConnector -Insertion failed. This Smart Bulb was already inserted. Updating the record.')
      return(self.updateBulb(newBulb))
      

  def updateBulb(self,bulb):
    
    now = (datetime.now() + timedelta(hours=+3))
    nowFormated = now.strftime('%Y-%m-%d %H:%M:%S')
    query = ("UPDATE Bulb SET LastModifiedDate = %s, Name = %s, Model = %s, Port = %s, Bright = %s,\
              Color_Mode = %s, CT = %s, Fw_Ver = %s, HUE = %s, Power = %s, RGB = %s,\
              Sat = %s, Support = %s, Effect = %s, Duration = %s, Auto_On = %s, Power_Mode = %s WHERE IP = %s")
    args = (nowFormated,bulb.Name,bulb.Model,bulb.Port,bulb.Bright,bulb.Color_Mode,bulb.CT,bulb.Fw_Ver,bulb.HUE,bulb.Power,bulb.RGB,bulb.Sat,bulb.Support,bulb.Effect,bulb.Duration,bulb.Auto_On,str(bulb.Power_Mode),bulb.IP)
    self.cursor.execute(query,args)
    return UPDATE_SUCCESS


#database = DatabaseConnector('localhost','smarthome','root','mateus12345')
#database.connect()
#database.createDataModel()
#database.disconnect()