from app import db

class Employee(db.Model):
    __tablename__ = 'Employee'

    id = db.Column(db.String(256), primary_key=True)
