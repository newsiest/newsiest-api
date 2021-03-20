from database import Base
from sqlalchemy import Column, Integer, String, DateTime

class NewsArticle(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    url = Column(String)
    img_url = Column(String)
    published_date = Column(DateTime)
    # tags = Column(postgresql.ARRAY)


# class Tag:
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String)

