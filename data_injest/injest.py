from threading import Thread
import pika
import time
import jsonpickle
from api.articles.models import NewsArticle, NewsSource

# Everything here happens on a separate thread

class DataParser:
    """
    Parses and stores incoming data into the db
    """
    def __init__(self, db):
        self._db = db

    def _get_source(self, inf=None):
        # Temp source, remove when source is passed in message
        inf = {
            'name': 'Sample Source',
            'img_url': 'blank'
        }
        slug = inf['name'].lower().replace(' ', '-')
        self._db.session.rollback()
        source = NewsSource.query.filter_by(slug=slug).first()

        if not source:
            self._db.session.rollback()
            source = NewsSource(**inf, slug=slug)
            self._db.session.add(source)

        return source

    def add_article(self, body):
        parsed = jsonpickle.decode(body)
        print(f'received:{parsed["title"]}')

        source = self._get_source()
        obj = NewsArticle(title=parsed['title'], author=parsed['author'], img_url=parsed['img_url'])
        obj.source = source

        if self._db:
            try:
                self._db.session.add(obj)
                self._db.session.commit()
            except:
                # Do nothing if article already exists
                pass


class DataFeed:
    """
    Handles incoming data from RabbitMQ
    """
    def __init__(self, db, url, queue_name):
        self._db = db
        self._parser = DataParser(db)
        self._params = pika.URLParameters(url)
        self._connection = None
        self._queue_name = queue_name

    def _connect(self):
        self._connection = pika.BlockingConnection(parameters=self._params)
        self._channel = self._connection.channel()
        self._channel.queue_declare(self._queue_name)
        self._channel.basic_consume(self._queue_name, self._callback, auto_ack=True)

    def _cleanup(self):
        pass

    def _callback(self, channel, method, properties, body):
        self._parser.add_article(body)

    def _run(self):
        self._connect()
        print("RabbitMQ Connected")
        self._channel.start_consuming()

    def start(self):
        Thread(target=self._run, daemon=True).start()