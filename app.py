from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

if __name__ == 'main':
    app.run(debug=True, port=3000)