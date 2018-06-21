from app.common.util.validation_util import is_empty
from app.common.domain.schema.error import Error

def validate_save_payload(data, key):
    errors = []
    if is_empty(data.get('name')):
        errors.append(Error('1012','Name must be present'))
    if is_empty(data.get('email')):
        errors.append(Error('1013','Email must be present'))
    return errors