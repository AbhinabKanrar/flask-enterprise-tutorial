from flask import Flask

app = Flask(__name__)

app.config.from_object('config')

from app.about.controller import about as about

app.register_blueprint(about)


@app.errorhandler(404)
def not_found(error):
    return "'error':'404'"