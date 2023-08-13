from src.models.User import user
from flask_jwt_extended import create_access_token
from src.errorHandler.Unauthorized import Unauthorized
from src.errorHandler.BadRequest import BadRequest

class UsersController:
    def __init__(self):
        pass

    def login(self, data):
        retUser = user.getByUsernameAndPassword(data.get("username"), data.get("password"))
        if retUser is None:
            raise Unauthorized(message="This user isn't exists or password is wrong")
        access_token = create_access_token(identity=retUser.get("id"))
        retUser['token'] = "Bearer " + access_token
        return retUser
        
    
    def signup(self, data):
        userExists = user.checkExistsByUsername(data.get("username"))
        if userExists is True:
            raise BadRequest("This user is already exists")
        userId = user.create([(data.get("name"), data.get("username"), data.get("password"))])
        retUser = user.getById(userId)
        access_token = create_access_token(identity=retUser.get("id"))
        retUser['token'] = "Bearer " + access_token
        return retUser
        
        

    