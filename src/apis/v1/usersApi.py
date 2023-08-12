from . import *
from datetime import datetime


usersMethods_bp = Blueprint('users', __name__, url_prefix='/v1/users')
controller = UsersController()

@usersMethods_bp.route('/login', methods=['POST'])
@swag_from('swagger/login.yml')
def login():
  try: 
    errors = loginValidation.validate(request.json)
    if(errors):
      raise BadRequest(payload={"errors": errors})
    
    user = controller.login(request.json)
    return Response.ok(data=user)

  except CustomError as e:
    if(e.message is not None):
      logger.error(e.message)
    raise e
  except Exception as e:
    logger.error(str(e))
    raise InternalServer()
  
@usersMethods_bp.route('/signup', methods=['POST'])
@swag_from('swagger/signup.yml')
def signup():
  try: 
    errors = signupValidation.validate(request.json)
    if(errors):
      raise BadRequest(payload={"errors": errors})
    
    if request.json.get("password") != request.json.get("password_confirmation"):
      raise BadRequest(message="password_confirmation doesn't equal to password")
    
    retUser = controller.signup(request.json)
    return Response.ok(data=retUser)

  except CustomError as e:
    if(e.message is not None):
      logger.error(e.message)
    raise e
  except Exception as e:
    logger.error(str(e))
    raise InternalServer()
