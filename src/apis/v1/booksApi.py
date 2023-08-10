from . import *


booksMethods_bp = Blueprint('books', __name__, url_prefix='/v1/books')
controller = BooksController()

@booksMethods_bp.route('/', methods=['GET'])
@swag_from('swagger/listBooks.yml')
def listBooks():
  try: 
    result = controller.list()
    return Response.ok(result)

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
    errors = getBookByIdValidation.validate({"id": id})
    if(errors):
      raise BadRequest(payload={"errors": errors})
    result = controller.get(id)
    if result is None:
      raise NotFound(message="This book doesn't exists")
    return Response.ok(result)

  except CustomError as e:
    if(e.message is not None):
      logger.error(e.message)
    raise e
  except Exception as e:
    logger.error(str(e))
    raise InternalServer()
  
@booksMethods_bp.route('/<id>', methods=['PUT'])
@swag_from('swagger/updateBook.yml')
def updateBook(id):
  try: 
    parameters = request.form.to_dict()
    parameters['id'] = id
    errors = getBookByIdValidation.validate(parameters)
    if(errors):
      raise BadRequest(payload={"errors": errors})
    
    name = request.args.get("name")
    price = request.args.get("price")
    release_date = request.args.get("release_date")
    category = request.args.get("category")
    
    data = {
      "name": name,
      "price": price,
      "release_date": release_date,
      "category": category,
      "id": id
    }
    
    result = controller.update(data)
    if result is False:
      raise NotFound(message="This book doesn't exist")
    return Response.ok(message="The book has been updated successfully")
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
    errors = createBookValidation.validate(request.args)
    if(errors):
      raise BadRequest(payload={"errors": errors})
    
    name = request.args.get("name")
    price = int(request.args.get("price"))
    release_date = request.args.get("release_date")
    category = request.args.get("category")
    author_id = int(request.args.get("author_id"))
    
    data = {
      "name": name,
      "price": price,
      "release_date": release_date,
      "category": category,
      "author_id": author_id
    }
    controller.insert(data)
    return Response.ok(message="The book has been created successfully")

  except CustomError as e:
    if(e.message is not None):
      logger.error(e.message)
    raise e
  except Exception as e:
    logger.error(str(e))
    raise InternalServer()
