from src.models.Book import book
from . import *

class BooksController:
    def __init__(self):
        pass

    def insert(self, data):
        author_id = data.get("author_id")
        userExists = author.checkExists(author_id)
        if userExists is False:
            raise NotFound(message="This author doesn't exists")
        
        book_data = [
            (
                data.get("name"), 
                data.get("price"), 
                data.get("release_date"), 
                data.get("category")
            )
        ]
        book_id = book.insert(book_data)
        book_authors_data = [
            (book_id, author_id)
        ]
        bookAuthors.insert(book_authors_data)
        print("The book has been inserted successfully and the id is {}".format(book_id))
    
    def list(self):
        return book.list()
    
    def get(self, id):
        return book.get(id)
    
    def update(self, data):
        result = book.checkExists(data.get("id"))
        if result is False:
            return False
        bookId = data.get('id')
        del data['id']
        book.update(bookId, data)
        

    