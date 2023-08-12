from . import *
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity


authorsMethods_bp = Blueprint('authors', __name__, url_prefix='/v1/authors')
controller = AuthorsController()

@authorsMethods_bp.route('/', methods=['GET'])
@swag_from('swagger/listAuthors.yml')
def listAuthors():
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
  
@authorsMethods_bp.route('/', methods=['POST'])
@jwt_required()
@swag_from('swagger/createAuthor.yml')
def createAuthor():
  try: 
    errors = createAuthorValidation.validate(request.args)
    if(errors):
      raise BadRequest(payload={"errors": errors})
    
    name = request.args.get("name")
    birthday = request.args.get("birthday")
    
    data = {
      "name": name,
      "birthday": birthday
    }
    controller.insert(data)
    return Response.ok(message="The author has been created successfully")

  except CustomError as e:
    if(e.message is not None):
      logger.error(e.message)
    raise e
  except Exception as e:
    logger.error(str(e))
    raise InternalServer()
