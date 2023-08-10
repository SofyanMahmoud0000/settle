from flask import Flask
# from flask_admin import Admin
from flasgger import Swagger
from flask_cors import CORS

from .config import settings
# from sqlalchemy import create_engine

app = Flask(__name__)
CORS(app,  resources={r"/v1/*": {"origins": "*"}})

def intiate_app():
    app.config['SWAGGER'] = {
    'title': settings.PROJECT_TITLE,
    'uiversion': 3
    }

    swagger = Swagger(app, template = settings.SWAGGER_TEMPLATE, config = settings.SWAGGER_CONFIG)


    app.config['SECRET_KEY'] = settings.SECRET_KEY
    __intiate_modules(app)
    return app

def __intiate_modules(app):
    from ..apis.v1.booksApi import booksMethods_bp
    from ..apis.v1.authorsApi import authorsMethods_bp
    app.register_blueprint(booksMethods_bp)
    app.register_blueprint(authorsMethods_bp)
