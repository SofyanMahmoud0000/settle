from . import *


class User(Connection):
  def __init__(self):
    super().__init__()
    
  def create(self, data):
    query = """INSERT INTO users(name, username, password) 
                VALUES (%s, %s, %s)"""
    
    return super().insert(query, data)
    
  def getByUsernameAndPassword(self, username, password):
    query = """SELECT * FROM users WHERE username = '{}' and password = '{}'""".format(username, password)
    cursor = super().select(query)
    data = cursor.fetchone()
    return self.convertUserToObject(data)
  
  def getById(self, id):
    query = """SELECT * FROM users WHERE id = {}""".format(id)
    cursor = super().select(query)
    data = cursor.fetchone()
    return self.convertUserToObject(data) 
    
  
  def convertUserToObject(self, userData):
    if userData is None:
      return None
    result = {
      "id": userData[0], 
      "name": userData[1], 
      "username": userData[2], 
      "password": userData[3]
      }
    return result
  
  def checkExistsById(self, id):
    query = "SELECT 1 FROM users WHERE id = {}".format(id)
    cursor = super().select(query)
    data = cursor.fetchone()
    return True if data is not None else False
  
  def checkExistsByUsername(self, username):
    query = "SELECT 1 FROM users WHERE username = '{}'".format(username)
    cursor = super().select(query)
    data = cursor.fetchone()
    return True if data is not None else False
  
user = User()
