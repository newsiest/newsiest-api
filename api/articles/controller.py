from flask import Blueprint

from ..utils.pagination import ResponseFormatter
from .services import ArticleService


view = Blueprint('articles', __name__)

@view.route('/')
def list():
    l = [a.as_dict() for a in ArticleService.get_all()]
    return ResponseFormatter.get_paginated(l)