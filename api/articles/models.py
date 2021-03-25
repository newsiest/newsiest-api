from app import db

class NewsSource(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    slug = db.Column(db.String(20), unique=True)
    name = db.Column(db.String(20))
    img_url = db.Column(db.String)
    articles = db.relationship('NewsArticle', lazy=True, backref=db.backref('source', lazy=False))

    __tablename__ = "sources"
    __table_args__ = {"schema": "news"}


class NewsArticle(db.Model):
    """Represents a news article"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    title = db.Column(db.String, unique=True)
    description = db.Column(db.Text)
    author = db.Column(db.String)
    url = db.Column(db.String)
    img_url = db.Column(db.String)
    published_date = db.Column(db.DateTime(timezone=True))
    source_id = db.Column(db.Integer, db.ForeignKey('news.sources.id'))

    __tablename__ = "articles"
    __table_args__ = {"schema": "news"}

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}




