from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class Person(db.Model):
    __tablename__ = 'person'
 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    student = db.Column(db.Boolean())
 
    def __init__(self, name, age, student):
        self.name = name
        self.age = age
        self.student = student
 
    def __repr__(self):
        return f"{self.name}:{self.age}:{self.student}"