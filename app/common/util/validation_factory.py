from app.common.util.validation_util import is_empty
from app.common.domain.schema.error import Error

def validate_save_payload(data, key):
    errors = []
    if is_empty(data.get('name')):
        errors.append(Error(code='1001',desc='Name must be present'))
    return errors