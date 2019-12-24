import os
from flask import Flask, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.geojson_flask
geodata_collection = db.geodata

database_name = os.environ['database_name']

@app.route('/geojson-features', methods=['GET'])
def get_all_points():
    features = []
    for geo_feature in geodata_collection.find({}):
        features.append({
            "type": "Feature",
            "geometry": {
                "type": geo_feature['geometry']['type'],
                "coordinates": geo_feature['geometry']['coordinates']
            }
        })

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html', database_name=database_name)

if __name__ == 'main':
    app.run(host='0.0.0.0')
