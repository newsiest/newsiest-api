from app import db


class NewsArticle(db.Model):
    """Represents a news article"""
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    author = db.Column(db.String)
    url = db.Column(db.String)
    img_url = db.Column(db.String)
    published_date = db.Column(db.DateTime)

    __table_args__ = {"schema": "news"}

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
