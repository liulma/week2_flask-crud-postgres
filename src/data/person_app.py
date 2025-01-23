from flask import Flask, jsonify, render_template,request
from flask_migrate import Migrate
from person_model import db, Person
from config import config
import json
 
app = Flask(__name__)

db_params = config()

db_uri = f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}"

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
 
@app.route("/", methods=["GET"])
def index():
    return {"index": True}

@app.route('/person', methods=['GET'])
def get_all_persons():
    try:  
        persons = Person.query.all()
        person_list = [{'id': p.id, 'name': p.name, 'age': p.age, 'student': p.student} for p in persons]
        return jsonify(person_list)
    except:
        return {"error": "no data"}

if __name__ == '__main__':
    app.run(debug=True)