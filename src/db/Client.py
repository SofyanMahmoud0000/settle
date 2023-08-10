from . import *


class Connection:
  connection = None
  cursor = None
  
  def __init__(self):
    if Connection.connection is None:
      Connection.connection = self.__createClient()
      logger.info("New connection connected to host {} with username {} and db {}".format(settings.DB_HOST, settings.DB_USERNAME, settings.DB_NAME))
      Connection.cursor = Connection.connection.cursor()
      
  def __createClient(self):
    connection = mysql.connector.connect(
      host=settings.DB_HOST,
      user=settings.DB_USERNAME,
      password=settings.DB_PASSWORD,
      database=settings.DB_NAME,
    )
    return connection
  
  def getCursor(self):
    return Connection.connection.cursor()
  
  def insert(self, query , values):
    logger.info("Inserting new data with query \n{} \n and values \n{}\n".format(query, values))
    Connection.cursor.executemany(query, values)
    Connection.connection.commit()
    return Connection.cursor.lastrowid
  
  def select(self, query):
    logger.info("Applying sellecting query \n{}".format(query))
    Connection.cursor.execute(query)
    return Connection.cursor
  
  def update(self, query):
    logger.info("Applying updating query \n{}".format(query))
    Connection.cursor.execute(query)
    Connection.connection.commit()
  