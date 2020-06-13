###############################################################################
# Name: DatabaseManager
#
#
##############################################################################
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

  # placeholder
  def newObject(self,name,description) :
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
    query = "CREATE TABLE IF NOT EXISTS Bulb (BulbId INT NOT NULL AUTO_INCREMENT, IP VARCHAR(15), Name VARCHAR(100), Model VARCHAR(20), Effect VARCHAR(10), Duration INT, Auto_On BOOLEAN, Power_Mode INTEGER, CONSTRAINT Id PRIMARY KEY(BulbId))"
    self.cursor.execute(query)

  def createDataModel(self):
    self.createSchema()
    self.useSchema()
    self.createTables()

#database = DatabaseConnector('localhost','smarthome','root','mateus12345')
#database.connect()
#database.createDataModel()
#database.disconnect()