from database.models import NewsArticle
from database import database as db

def get_all(limit=10, offset=0, **kwargs):
    session = db.get_session()
    return list(session.query(NewsArticle).order_by(NewsArticle.id))

# print(get_all())
