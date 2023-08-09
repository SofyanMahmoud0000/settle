from .CustomError import CustomError

class InternalServer(CustomError):
  status_code = 500
  
  def getDefaultMessage(self):
    return "Internal error, try again or see the logs"
    
    