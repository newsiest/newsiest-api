from flask import Flask

from routes import index, articles

app = Flask(__name__)
app.config['DEBUG'] = True

app.register_blueprint(index.view, url_prefix='/')
app.register_blueprint(articles.view, url_prefix='/articles')

if __name__ == 'main':
    print('start')
    app.run(debug=True, port=3000)