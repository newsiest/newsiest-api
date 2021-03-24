from .models import NewsArticle


class ArticleService:

    @staticmethod
    def get_all(**kwargs):
        return NewsArticle.query.order_by(NewsArticle.published_date.desc())