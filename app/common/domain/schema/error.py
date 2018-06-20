from app import ma

class Error:

    def __init__(self, code, desc):
        self.code = code
        self.desc = desc

class ErrorSchema(ma.Schema):
    class Meta:
        fields = ('code', 'desc')