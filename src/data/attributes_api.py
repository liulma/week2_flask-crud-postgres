from flask import Flask, request
from attributes_service import db_get_attributes, db_get_attribute_by_id, db_create_attribute, db_update_attribute

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return {"index": True}

@app.route('/attributes', methods=['GET'])
def get_all_attributes():
    try:  
        return db_get_attributes()
    except:
        return {"error": "no data"}

@app.route('/attributes/<int:id>', methods=['GET'])
def get_attribute_by_id(id):
    try:
        return db_get_attribute_by_id(id)
    except:
        return {"error": "no attribute with id %s" % id}
    
@app.route("/attributes", methods=['POST'])
def create_attribute():
    try: 
        data = request.get_json()
        attribute_name = data['attribute_name']
        attribute_description = data['attribute_description']
        attribute_value = data['attribute_value']
        person_id = data['person_id']
        db_create_attribute(attribute_name, attribute_description, attribute_value, person_id)
        return {"success": "created attribute: %s" % attribute_name}
    except:
        return {"error": "error creating attribute"}
    
@app.route("/attributes/<int:id>", methods=['PUT'])
def update_attribute(id):
    try:
        data = request.get_json()
        attribute_name = data['attribute_name']
        attribute_description = data['attribute_description']
        attribute_value = data['attribute_value']
        person_id = data['person_id']
        db_update_attribute(id, attribute_name, attribute_description, attribute_value, person_id)
        return {"success": "updated person"}
    except:
        return {"error": "error updating person"}
    
if __name__ == "__main__":
    app.run()