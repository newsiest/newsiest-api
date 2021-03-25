from threading import Thread

# Everything here happens on a separate thread

class DataFeed:

    def __init__(self, db):
        self.db = db

    def _connect(self):
        pass

    def _cleanup(self):
        pass

    def _receive(self, article):
        pass

    def _run(self):
        self._connect()
        # ...
        pass

    def start(self):

        pass