from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Openshift stuff',
        'description': 'contains lots of stuff'
    },
    {
        'id': 2,
        'title': 'More Openshift stuff',
        'description': 'contains more stuff'
    },
    {
        'id': 3,
        'title': 'Linux stuff',
        'description': 'contains Linux stuff'
    },
    {
        'id': 4,
        'title': 'Windows stuff',
        'description': 'contains Windows stuff'
    }
]

@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == 'main':
    app.run(host='0.0.0.0')
