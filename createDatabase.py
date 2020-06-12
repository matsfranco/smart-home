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

  # placeholder
  def createDataModel(self):
    self.createSchema()
    self.useSchema()

try:
  database = DatabaseConnector('localhost','smarthome','root','mateus12345')
  database.connect()
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:

  database.createDataModel()
  database.disconnect()