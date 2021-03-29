from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

from threading import Thread
import time

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
Migrate(app, db)

from api.articles import models
from api.articles import controller as articles

app.register_blueprint(articles.view, url_prefix='/articles')

from data_injest import injest
injest.DataFeed().start()


if __name__ == 'main':
    print('start')
    app.run(debug=True, port=3000)