import json
from flask import Blueprint

view = Blueprint('test', __name__)

@view.route('/')
def index_():
    return (json.dumps({ 'message': "Hello friend!" }),
        200, { 'content_type': 'application/json'})

