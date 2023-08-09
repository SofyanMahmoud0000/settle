from . import *


class Connection:
  connection = None
  
  def __init__(self):
    if Connection.connection is None:
      Connection.connection = self.__createClient()
      logger.info("New connection connected to host {} with username {} and db {}".format(settings.DB_HOST, settings.DB_USERNAME, settings.DB_NAME))
      
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
