import sqlite3

from flask import Flask, Blueprint, request, Response, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

from views.api import api
from database import connection

# Before <any> request
@app.before_request
def before_request():
    connection.connect()

# After <any> request
@app.after_request
def after_request(response):
    connection.close()
    return response

# Index
@app.route('/', methods=['GET'])
def app_index():
    return render_template('index.html')

# 500
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

# 502
@app.errorhandler(502)
def server_error(e):
    return render_template('500.html'), 500

# 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# API Routes
app.register_blueprint(api, url_prefix='/api/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
