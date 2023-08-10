from src.models.Author import author

class AuthorsController:
    def __init__(self):
        pass

    def insert(self, data):
        data = [
            (
                data.get("name"), 
                data.get("birthday")
            )
        ]
        author_id = author.insert(data)
        print("The author has been inserted successfully and the id is {}".format(author_id))
    
    def list(self):
        return author.list()
        

    