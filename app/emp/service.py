from app.common.entity.emp import Employee
from app import db

def save():
    print('cool paglu')
    emp = Employee(name='n1',email='e1')
    db.session.add(emp)
    db.session.commit()