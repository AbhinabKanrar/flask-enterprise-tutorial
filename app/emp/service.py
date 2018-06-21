from app.common.entity.emp import Employee
from app.common.domain.schema.generic_response import Response
from app.common.util.validation_util import is_empty
from app import db

import app.common.util.validation_factory as validation
import app.emp.dao as dao

def save(data, siteId):
    errors = validation.validate_save_payload(data, siteId)
    
    resp = Response()

    if is_empty(errors) == False:
        for error in errors:
            resp.add_error(error)

    emp = Employee(name=data.get('name'), email=data.get('email'), site=siteId)
    
    try:
        dao.save(emp)
    except (RuntimeError, OSError) as err:
        print("error: {0}".format(err))
    
    return resp
