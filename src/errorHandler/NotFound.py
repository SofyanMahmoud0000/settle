from .CustomError import CustomError

class NotFound(CustomError):
    status_code = 404
