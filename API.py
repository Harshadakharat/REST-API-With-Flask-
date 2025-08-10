from flask import Flask, jsonify, request 
app = Flask(__name__)


todos = [
    {"id": 1, "task": "Learn Flask", "done": False},
    {"id": 2, "task": "Build an API", "done": False}
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Todo API"})


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo:
        return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404


@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_todo = {
        "id": len(todos) + 1,
        "task": data.get("task", ""),
        "done": False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    data = request.get_json()
    todo["task"] = data.get("task", todo["task"])
    todo["done"] = data.get("done", todo["done"])
    return jsonify(todo)


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"message": "Todo deleted"})


if __name__ == '_main_':
    app.run(debug=True)