from . import *


class BookAuthors(Connection):
  def __init__(self):
    super().__init__()
    
  def insert(self, data):
    query = """INSERT INTO book_authors(book_id, author_id) 
                VALUES (%s, %s)"""
    return super().insert(query, data)
    
  def listBooks(self):
    self.insert()
  
bookAuthors = BookAuthors()
