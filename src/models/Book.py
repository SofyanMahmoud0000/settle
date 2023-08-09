from . import *


class Book(Connection):
  def __init__(self):
    super().__init__()
    self.cursor = self.getCursor()
  
book = Book()
