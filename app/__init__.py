from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('config.settings')
app.config.from_envvar('FLASK_ENV',silent=True)

db = SQLAlchemy(app)

from app.emp.controller import emp as emp

app.register_blueprint(emp)


@app.errorhandler(404)
def not_found(error):
    return "'error':'404'"