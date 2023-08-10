from . import *
from datetime import datetime


authorsMethods_bp = Blueprint('authors', __name__, url_prefix='/v1/authors')
controller = AuthorsController()

@authorsMethods_bp.route('/', methods=['GET'])
@swag_from('swagger/listAuthors.yml')
def listAuthors():
  try: 
    result = controller.list()
    print("The result of listing the authors is: {}".format(result))
    return Response.ok(result)

  except CustomError as e:
    if(e.message is not None):
      logger.error(e.message)
    raise e
  except Exception as e:
    logger.error(str(e))
    raise InternalServer()
  
@authorsMethods_bp.route('/', methods=['POST'])
@swag_from('swagger/createAuthor.yml')
def createAuthor():
  try: 
    name = request.args.get("name")
    birthday = request.args.get("birthday")
    
    data = {
      "name": name,
      "birthday": birthday
    }
    controller.insert(data)
    return Response.ok("Create book API")

  except CustomError as e:
    if(e.message is not None):
      logger.error(e.message)
    raise e
  except Exception as e:
    logger.error(str(e))
    raise InternalServer()
