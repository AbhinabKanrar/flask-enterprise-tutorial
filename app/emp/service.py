from app.common.entity.emp import Employee
from app.common.domain.schema.generic_response import Response
from app.common.util.validation_util import is_empty
from app import db

import app.common.util.validation_factory as validation

def save(data, siteId):
    errors = validation.validate_save_payload(data, siteId)
    
    resp = Response(False, None, None)

    if is_empty(errors) == False:
        resp.errors = errors

    emp = Employee(name='n3',email='e3',site='s3')
    
    try:
        db.session.add(emp)
        db.session.commit()
    except (RuntimeError, TypeError, OSError) as err:
        print("error: {0}".format(err))
    
    return resp
