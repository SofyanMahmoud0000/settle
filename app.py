from src.config import intiate_app
from src.config.config import settings


port = settings.PORT
app = intiate_app()
from src.models import *

if __name__ == "__main__":
    app.debug = True
    app.run(host=settings.HOST, port=settings.PORT)