import os
from app import app

PORT = int(os.environ.get('FLASK_SERVER_PORT', '8080'))

app.run(port=PORT)