from . import *


class Book(Connection):
  def __init__(self):
    super().__init__()
    
  def insert(self, data):
    query = """INSERT INTO books(name, price, release_date, category) 
                VALUES (%s, %s, %s, %s)"""
    return super().insert(query, data)
    
  def list(self):
    query = """SELECT * FROM books"""
    cursor = super().select(query)
    data = cursor.fetchall()
    result = [{
        "id": element[0], 
        "name": element[1], 
        "price": element[2],
        "release_date": element[3],
        "category": element[4]
       } for element in data]
    return result
  
  def get(self, id):
    query = """SELECT * FROM books WHERE id={}""".format(id)
    cursor = super().select(query)
    data = cursor.fetchone()
    if data is None:
      return None
    result = {
        "id": data[0], 
        "name": data[1], 
        "price": data[2],
        "release_date": data[3],
        "category": data[4]
       }
    return result
  
  def update(self, id, data):
    query = """UPDATE books set """
    for key in data:
      if data[key] is not None:
        tmp = """{} = '{}',""".format(key, data[key])
        query += tmp
    query = query[0: -1]
    query += " WHERE id = {}".format(id)
    super().update(query)
    
  def checkExists(self, id):
    query = "SELECT 1 FROM books WHERE id = {}".format(id)
    cursor = super().select(query)
    data = cursor.fetchone()
    return True if data is not None else False
    
    
book = Book()
