from flask import Flask, request
from attributes_service import db_get_attributes, db_get_attribute_by_id

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
        return {"error": "no person with id %s" % id}
    
if __name__ == "__main__":
    app.run()