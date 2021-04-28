from flask import Blueprint, request

from ..utils.pagination import ResponseFormatter
from .services import ArticleService
from ..utils.auth import check_auth

view = Blueprint('articles', __name__)

@view.route('/')
def list():
    l = [a.as_dict() for a in ArticleService.get_all()]
    return ResponseFormatter.get_paginated(l)



@view.route('/lock/')
@check_auth
def lock(user=None):
    l = [a.as_dict() for a in ArticleService.get_all()]

    return ResponseFormatter.get_paginated(l)

