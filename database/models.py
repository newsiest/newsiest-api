from database.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Text


class NewsArticle(Base):
    """Represents a news article"""
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(Text)
    author = Column(String)
    url = Column(String)
    img_url = Column(String)
    published_date = Column(DateTime)

    __table_args__ = {"schema": "news"}

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

