from flask import Flask

from routes import index

import database

app = Flask(__name__)
app.config['DEBUG'] = True

app.register_blueprint(index.index, url_prefix='/')

if __name__ == 'main':
    print('start')
    app.run(debug=True, port=3000)