from . import *


class CreateBookValidations(Schema):
  """
  Parameters:
    - name (datetime)
    - price (datetime)
    - release_date (int)
    - category (int)
    - author_id (int)
  """
  
  name = fields.String(required=True)
  price = fields.Int(required=True)
  release_date = fields.Date(required=True)
  category = fields.String(required=True)
  author_id = fields.Int(required=True)
   
createBookValidation = CreateBookValidations()