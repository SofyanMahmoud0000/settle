from . import *


class SignupValidation(Schema):
  """
  Parameters:
    - name (string)
    - username (string)
    - password (string)
    - password_confirmation (string)
  """
  
  name = fields.String(required=True)
  username = fields.String(required=True)
  password = fields.String(required=True)
  password_confirmation = fields.String(required=True)
  
signupValidation = SignupValidation()


class LoginValidation(Schema):
  """
  Parameters:
    - username (string)
    - password (int)
  """
  
  username = fields.String(required=True)
  password = fields.String(required=True)
   
loginValidation = LoginValidation()

