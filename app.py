from flask import jsonify

from config import app, db, RABBIT_URL
from api.articles import controller as articles
from api.utils.exceptions import APIException
from data_injest import injest

app.register_blueprint(articles.view, url_prefix='/articles')

injest.DataFeed(db=db, url=RABBIT_URL, queue_name='articles').start()

# TODO cleanup this entire file and properly check env vars


@app.errorhandler(APIException)
def handle_api_exception(ex):
    response = jsonify({'message': ex.message})
    response.status_code = ex.status_code
    return response


if __name__ == 'main':
    print('start')
    app.run(debug=True, port=3000)