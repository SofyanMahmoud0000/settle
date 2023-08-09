import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    SWAGGER_TEMPLATE = {
        "swagger": "2.0.5",
        "info": {
            "title": os.getenv('PROJECT_TITLE'),
            "description": os.getenv('PROJECT_DESCRIPTION'),
            "contact": {
            "responsibleOrganization": "Settle",
            "responsibleDeveloper": "Sofyan Mahmoud",
            "email": "sofyan1020@gmail.com",
            },
            "version": "0.1.0",
            'uiversion': 3
        },
        "host": os.getenv("HOST_URL"),
        "basePath": "/",
        "schemes": [
            "http",
            "https"
        ],
        "operationId": "CRUD Operations",
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "\
                JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
            }
        },
        "security": [
            {
                "Bearer": []
            }
            ]
        }

    SWAGGER_CONFIG = {
        "headers": [
        ],
        "specs": [
            {
                "endpoint": 'apispecs',
                "route": '/apispecs.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        # "static_folder": "static",  # must be set by user
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }

    PROJECT_NAME: str = os.getenv('PROJECT_NAME')
    PROJECT_TITLE: str = os.getenv('PROJECT_TITLE')
    PROJECT_DESCRIPTION: str = os.getenv('PROJECT_DESCRIPTION')
    PROJECT_VERSION: str = os.getenv('PROJECT_VERSION')

    PORT: int =os.getenv("PORT")
    
    HOST: str =os.getenv("HOST")

    DB_HOST = os.getenv("DB_HOST")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    SECRET_KEY = os.getenv("SECRET_KEY")
    
    DEBUG = True if os.getenv("DEBUG") == "True" else False
    
settings = Settings()
