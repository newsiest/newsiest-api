import json
from flask import Blueprint

import database as db

index = Blueprint('test', __name__)

@index.route('/')
def index_():
    return (json.dumps({ 'message': "Hello friend!" }),
        200, { 'content_type': 'application/json'})

