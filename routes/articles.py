import json
from flask import Blueprint

from services import articles

view = Blueprint('articles', __name__)

@view.route('/')
def list():
    l = [a.as_dict() for a in articles.get_all()]
    return json.dumps(l)