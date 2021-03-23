from database import Base, engine, create_db
from sqlalchemy import Column, Integer, String, DateTime, Text

class NewsArticle(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(Text)
    author = Column(String)
    url = Column(String)
    img_url = Column(String)
    published_date = Column(DateTime)

    __table_args__ = {"schema": "news"}

