from .CustomError import CustomError

class BadRequest(CustomError):
    status_code = 400