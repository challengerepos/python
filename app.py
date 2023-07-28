from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data - We'll use a list to store the data
data = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'},
    {'id': 3, 'name': 'Item 3'},
]

# GET all items
@app.route('/api/items', methods=['GET'])
def get_all_items():
    return jsonify(data)

# GET a single item by ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_single_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# POST a new item
@app.route('/api/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    new_item['id'] = len(data) + 1
    data.append(new_item)
    return jsonify(new_item), 201

# PUT (update) an item by ID
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        updated_item = request.get_json()
        item.update(updated_item)
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# DELETE an item by ID
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [item for item in data if item['id'] != item_id]
    return jsonify({'message': 'Item deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
