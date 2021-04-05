from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Flask
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
Migrate(app, db)

# RabbitMQ
RABBIT_URL = 'amqp://guest:guest@localhost:5672/%2f' # TODO get from env

# Auth0 setup
AUTH0_DOMAIN = 'newsiest.us.auth0.com'
API_AUDIENCE = 'https://newsiest.us.auth0.com/api/v2/'
ALGORITHMS = ["RS256"]
