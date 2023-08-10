from . import *


class Author(Connection):
  def __init__(self):
    super().__init__()
    
  def insert(self, data):
    query = """INSERT INTO authors(name, birthday) 
                VALUES (%s, %s)"""
    return super().insert(query, data)
    
  def list(self):
    query = """SELECT * FROM authors"""
    cursor = super().select(query)
    data = cursor.fetchall()
    result = [{"name": element[1], "birthday": element[2]} for element in data]
    return result
  
author = Author()
