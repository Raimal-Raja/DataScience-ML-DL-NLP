# Put and delete HTTP Verbs
# Working with API--Json

from flask import Flask, request, jsonify

app = Flask(__name__)

#initil data in my to do list

items =[
    {'ID': 1,"Name":"Item 1", "Description":"This is item1"},
    {'ID': 2,"Name":"Item 2", "Description":"This is item2"}
    ]


@app.route('/')
def home():
    return "Welcome to TODO-list"

# get: retreive all the items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get: Retreive a specific item by ID
@app.route('/items/<int:item_id', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['ID']==item_id), None)
    if item is None:
        return jsonify({"Error": "Item not found"})
    return jsonify(item)

# POST: create a new task
@app.route('/items', methods=['POST'])
def create_new_task():
     if not request.json or not 'name' in request.json:
         return jsonify({"Error": "Item not found"})
     new_item = {
         'ID':items[-1]['ID']+1 if items else 1,
         'name':request.json['name'],
         "Description":request.json['Description']
     }
     items.append(new_item)
     return jsonify(new_item)
 
 
# Put: Updated an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['ID']==item_id), None)
    if item in None:
        return jsonify({"Error": "Item not found"})
    item['name'] = request.json.get('name', item['name'])    


if __name__=="__main__":
    app.run(debug=True)