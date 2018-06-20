from app import db

class Employee(db.Model):
    __tablename__ = 'Employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    site = db.Column(db.String(255), nullable=False)

def __init__(self, name, email, site):
   self.name = name
   self.email = email
   self.site = site
