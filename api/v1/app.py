#!/usr/bin/python3
""" Setup API, import, register blueprint, declare methods, run server """
from flask import Flask, render_template, Blueprint, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": '0.0.0.0'}})
app.register_blueprint(app_views, url_prefix='/api/v1')
""" Flask app has global config object that is accessed through app.config """
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
""" jsonify responses will be output with newlines, spaces, and indentation """
""" helps with easier reading for humans """


@app.teardown_appcontext
def teardown(context):
    """ Will only run when app is done """
    storage.close()


@app.errorhandler(404)
def error404(e):
    """ Will return a 404 error """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    realport = getenv('HBNB_API_PORT')
    if host is None:
        host = '0.0.0.0'
    if realport is None:
        realport = '5000'
    app.run(debug=True, host=host, port=realport, threaded=True)
