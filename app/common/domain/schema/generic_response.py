class Response:
    
    def __init__(self, status, data, errors):
        self.status = status
        self.data = data
        self.errors = errors