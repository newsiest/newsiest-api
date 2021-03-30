from threading import Thread

import pika
import time
import jsonpickle
from api.articles.models import NewsArticle

# Everything here happens on a separate thread

class DataFeed:

    def __init__(self, db):
        self.db = db

    def _connect(self):
        pass

    def _cleanup(self):
        pass

    def _callback(self, channel, method, properties, body):
        parsed = jsonpickle.decode(body)
        obj = NewsArticle(title=parsed['title'], author=parsed['author'], img_url=parsed['img_url'])
        if self.db:
            self.db.session.add(obj)
            self.db.session.commit()

    def _run(self):
        while True:
            try:
                self._connect()
                print("RabbitMQ Connected")
                self.channel.start_consuming()
                break
            except:
                time.sleep(5)
                print("Not connected")
                pass

    def start(self):
        Thread(target=self._run).start()
        pass