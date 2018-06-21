class Response:

    def __init__(self):
        self.status = False
        self.data = None
        self.errors = []
    
    def add_error(self, error):
        self.errors.append(error.__dict__)