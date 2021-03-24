from .models import NewsArticle


class ArticleService:

    @staticmethod
    def get_all(limit=10, offset=0, **kwargs):
        return NewsArticle.query.order_by(NewsArticle.published_date)