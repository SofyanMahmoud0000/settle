from . import *


class CreateAuthorValidation(Schema):
  """
  Parameters:
    - name (string)
    - birthday (int)
  """
  
  name = fields.String(required=True)
  birthday = fields.Date(required=True)
   
createAuthorValidation = CreateAuthorValidation()

