from threading import Thread
import os
import pika

# Everything here happens on a separate thread

class DataFeed:
    QUEUE_NAME = 'articles'

    def __init__(self, db = None, url = None):
        self.db = db
        self.url = url

        self.connection = None
        self.channel = None

    def _connect(self):
        self.connection = pika.BlockingConnection()
        self.channel = self.connection.channel()
        self.channel.queue_declare(self.QUEUE_NAME)
        self.channel.basic_consume(self.QUEUE_NAME, self._callback)

    def _callback(self, channel, method, properties, body):
        print(" [x] Received " + str(body))

    def _run(self):
        self._connect()
        self.channel.start_consuming()

    def start(self):
        Thread(target=self._run).start()
        pass


# Thread(target=lambda: DataFeed(None).start()).start()

# def on_message(channel, method_frame, header_frame, body):
#     print(method_frame.delivery_tag)
#     print(body)
#     print()
#     channel.basic_ack(delivery_tag=method_frame.delivery_tag)
#
#
# connection = pika.BlockingConnection()
# channel = connection.channel()
# channel.queue_declare(queue='articles')
# channel.basic_consume('articles', on_message)
# try:
#     channel.start_consuming()
# except KeyboardInterrupt:
#     channel.stop_consuming()
# connection.close()