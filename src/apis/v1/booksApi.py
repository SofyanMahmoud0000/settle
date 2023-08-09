from . import *


booksMethods_bp = Blueprint('books', __name__, url_prefix='/v1/books')
controller = BooksController()

@booksMethods_bp.route('/', methods=['GET'])
@swag_from('swagger/listBooks.yml')
def listBooks():
  try: 
    return Response.ok("List books API")

  except CustomError as e:
    if(e.message is not None):
      logger.error(e.message)
    raise e
  except Exception as e:
    logger.error(str(e))
    raise InternalServer()
  
@booksMethods_bp.route('/<id>', methods=['GET'])
@swag_from('swagger/getBook.yml')
def getBook(id):
  try: 
    return Response.ok("Get book API")

  except CustomError as e:
    if(e.message is not None):
      logger.error(e.message)
    raise e
  except Exception as e:
    logger.error(str(e))
    raise InternalServer()
  
@booksMethods_bp.route('/', methods=['PUT'])
@swag_from('swagger/updateBook.yml')
def updateBook():
  try: 
    return Response.ok("Update book API")

  except CustomError as e:
    if(e.message is not None):
      logger.error(e.message)
    raise e
  except Exception as e:
    logger.error(str(e))
    raise InternalServer()
  
@booksMethods_bp.route('/', methods=['POST'])
@swag_from('swagger/createBook.yml')
def createBook():
  try: 
    return Response.ok("Create book API")

  except CustomError as e:
    if(e.message is not None):
      logger.error(e.message)
    raise e
  except Exception as e:
    logger.error(str(e))
    raise InternalServer()
