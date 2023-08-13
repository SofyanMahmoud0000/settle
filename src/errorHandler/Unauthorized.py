from .CustomError import CustomError

class Unauthorized(CustomError):
    status_code = 401