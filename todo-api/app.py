#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

# START YOUR FLASK PROJECT FROM HERE

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    },
    {
        'id': 3,
        'title': u'Flutter Karo',
        'description': u'Need to Flutter on the web', 
        'done': False
    }
]

@app.route('/todo/api/tasks', methods=['GET']) # this function gets called at localhost:5000/todo/api/v1.0/tasks when called by GET method (from simpleHTTP Server)
def get_tasks():
    return jsonify({'tasks': tasks}) # creates a dictionary with key 'tasks' and value <LIST OF TASKS>

from flask import abort

@app.route('/todo/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)	# Task not found (invalid task_id in URL)
    return jsonify({'task': task[0]})

# POST METHODS

from flask import request

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': tasks}), 201



# OUT OF BOUNDS FROM HERE !!!! KEEP IT AS-IS IN EVERY FLASK PROJECT !

from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
