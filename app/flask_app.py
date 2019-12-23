from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Openshift stuff',
        'description': 'contains lots of stuff'
    },
    {
        'id': 2,
        'title': 'More stuff',
        'description': 'contains more stuff'
    },
    {
        'id': 3,
        'title': 'Linux stuff',
        'description': 'contains Linux stuff'
    },
    {
        'id': 4,
        'title': 'Mac stuff',
        'description': 'contains Mac stuff'
    }
]

@app.route('/', methods=['GET'])
def get_tasks():
    client = MongoClient()
    return jsonify({'tasks': tasks})

if __name__ == 'main':
    app.run(host='0.0.0.0')
