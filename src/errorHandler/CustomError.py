class CustomError(Exception):
  def __init__(self, message = None, payload=None):
    super().__init__()
    self.message = message or self.getDefaultMessage()
    self.payload = payload
    self.success = False

  def to_dict(self):
    rv = dict(self.payload or ())
    rv['success'] = self.success
    if self.message is not None:
      rv['message'] = self.message
    return rv
  
  def getDefaultMessage(self):
    return None
      
    