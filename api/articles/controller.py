from flask import Blueprint
import json

from .service import ArticleService

view = Blueprint('articles', __name__)

@view.route('/')
def list():
    l = [a.as_dict() for a in ArticleService.get_all()]
    return json.dumps(l)