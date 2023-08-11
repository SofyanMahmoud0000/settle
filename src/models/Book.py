from . import *


class Book(Connection):
  def __init__(self):
    super().__init__()
    
  def insert(self, data):
    query = """INSERT INTO books(name, price, release_date, category) 
                VALUES (%s, %s, %s, %s)"""
    return super().insert(query, data)
    
  def list(self, data):
    
    queryForTotalCount = """ select count(*) from books b
        join book_authors ba on ba.book_id = b.id
        join authors a on a.id = ba.author_id 
        where a.name like '%{}%' 
        and category like '%{}%'
        and b.name like '%{}%'
        and price >= {} and price <= {}
        and release_date >= '{}' and release_date <= '{}'
        """.format(
          data.get("author_name"),
          data.get("category"),
          data.get("name"),
          data.get("minimum_price"), 
          data.get("maximum_price"),
          data.get("oldest_date"),
          data.get("earliest_date"),
        )
        
    cursor = super().select(queryForTotalCount)
    count = cursor.fetchone()[0]
    
    
    query = """ select b.*, a.name as author_name from books b
        join book_authors ba on ba.book_id = b.id
        join authors a on a.id = ba.author_id 
        where a.name like '%{}%' 
        and category like '%{}%'
        and b.name like '%{}%'
        and price >= {} and price <= {}
        and release_date >= '{}' and release_date <= '{}'
        limit {} offset {}
        """.format(
          data.get("author_name"),
          data.get("category"),
          data.get("name"),
          data.get("minimum_price"), 
          data.get("maximum_price"),
          data.get("oldest_date"),
          data.get("earliest_date"),
          data.get("pageSize"),
          data.get("pageSize") * (data.get("pageNo") - 1)
        )
    
    cursor = super().select(query)
    data = cursor.fetchall()
    result = [{
        "id": element[0], 
        "name": element[1], 
        "price": element[2],
        "release_date": element[3],
        "category": element[4],
        "author_name": element[5],
       } for element in data]
    return result, count
  
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
