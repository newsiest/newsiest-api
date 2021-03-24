from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from old_routes import index, articles


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/newsiest-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
Migrate(app, db)


from api.articles import models
# db.create_all()

# app.register_blueprint(index.view, url_prefix='/')
# app.register_blueprint(articles.view, url_prefix='/articles')

from api.articles import controller as articles
app.register_blueprint(articles.view, url_prefix='/articles')


if __name__ == 'main':
    print('start')
    app.run(debug=True, port=3000)