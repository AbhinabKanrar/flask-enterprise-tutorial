from app.common.entity.emp import Employee
from app import db

def save(data, siteId):
    print('********************************')
    print(siteId)
    print(data.get('key'))
    print('********************************')

    emp = Employee(name='n3',email='e3',site='s3')
    db.session.add(emp)
    db.session.commit()