from flask import jsonify
from src.config import app
from .CustomError import CustomError

@app.errorhandler(CustomError)
def errorListener(e):
    return jsonify(e.to_dict()), e.status_code