import os

from bson import ObjectId
from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# load environment config values
env_name = os.environ.get('ENV_NAME', '.env did not load')
MONGO_USERNAME = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
MONGO_PASSWORD = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')

client = MongoClient(f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@mongo:27017/')

db = client.flask_db
todos = db.todos


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        item = request.form['item']
        todos.insert_one({'item': item})
    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)


@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))


@app.route('/env')
def get_env():
    data = {'env_name': f'{env_name}'}
    return jsonify(data)


@app.route('/hello')
def hello():
    return jsonify({'hello': 'world'})


if __name__ == "__main__":
    app.run()
