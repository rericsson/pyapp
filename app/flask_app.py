import os
import sys
from flask import Flask, jsonify, render_template
from flask_debugtoolbar import DebugToolbarExtension
from pymongo import MongoClient

app = Flask(__name__)
try:
    debug = os.environ['FLASK_ENV']
    if debug == 'development':
        app.logger.info("FLASK_ENV=development")
        app.secret_key = '123456789'
        toolbar = DebugToolbarExtension(app)
except KeyError:
    app.logger.info("FLASK_ENV not set")

try:
    database_name = os.environ['database_name']
    database_username = os.environ['username']
    database_password = os.environ['password']
    database_uri = os.environ['uri']
except KeyError:
    print("Error: please set the database env variables", file=sys.stderr)
    sys.exit(1)

client = MongoClient(database_uri,
                     username=database_username,
                     password=database_password,
                     authSource=database_name)
db = client.pyapp
geodata_collection = db.geodata


@app.route('/geojson-features', methods=['GET'])
def get_all_points():
    features = []
    for geo_feature in geodata_collection.find({}):
        features.append({
            "coordinates": geo_feature['coordinates'],
            "type": geo_feature['type']
        })
    return jsonify(features)

@app.route('/', methods=['GET'])
def main():
    app.logger.warning("Message in Flask Debugger")
    return render_template('main.html', database_name=database_name)

if __name__ == 'main':
    app.run(host='0.0.0.0')
