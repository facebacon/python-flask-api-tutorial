from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    # Return the JSON representation of the todos list
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    # Parse the request body into a Python dictionary
    request_body = request.json
    print("Incoming request with the following body:", request_body)
    
    # Add the new todo to the global todos list
    todos.append(request_body)
    
    # Return the updated todos list in JSON format
    return jsonify(todos), 200  # Return 200 OK

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    
    # Check if the position is valid (within the range of the todos list)
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 400  # Return 400 if out of bounds
    
    # Remove the todo at the specified position
    deleted_todo = todos.pop(position)
    
    # Return the updated todos list in JSON format
    return jsonify(todos), 200  # Return 200 OK


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)