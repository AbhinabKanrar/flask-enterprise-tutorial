from app import db

class Employee(db.Model):
    __tablename__ = 'Employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

def __init__(self, name, email):
   self.name = name
   self.email = email
