from . import *


class CreateBookValidations(Schema):
  """
  Parameters:
    - name (string)
    - price (int)
    - release_date (date)
    - category (string)
    - author_id (int)
  """
  
  name = fields.String(required=True)
  price = fields.Int(required=True)
  release_date = fields.Date(required=True)
  category = fields.String(required=True)
  author_id = fields.Int(required=True)
   
createBookValidation = CreateBookValidations()

class UpdateBookValidations(Schema):
  """
  Parameters:
    - name (string)
    - price (int)
    - release_date (date)
    - category (string)
    - id (int)
  """
  
  name = fields.String()
  price = fields.Int()
  release_date = fields.Date()
  category = fields.String()
  author_id = fields.Int(required=True)
   
updateBookValidation = UpdateBookValidations()


class GetBookByIdValidation(Schema):
  """
  Parameters:
    - id (int)
  """
  
  id = fields.Int(required=True)
  
getBookByIdValidation = GetBookByIdValidation()
  
