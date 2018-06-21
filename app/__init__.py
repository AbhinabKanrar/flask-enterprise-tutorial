from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig

from app.common.domain.schema.error import Error
from app.common.util.resp_mapper import create_resp

import logging


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

app.config.from_object('config.settings')
app.config.from_envvar('FLASK_ENV',silent=True)

logger = logging.getLogger('FlaskLogger')
logger.addHandler(logging.handlers.TimedRotatingFileHandler('flask.log', when="d", interval=1, backupCount=5))

db = SQLAlchemy(app)

from app.common.entity.emp import Employee

db.create_all()
db.session.commit()

from app.emp.controller import emp as emp

app.register_blueprint(emp)

@app.errorhandler(404)
def not_found(error):
    return create_resp(Error('1001','NOT_FOUND'), 404)

@app.errorhandler(400)
def bad_data(error):
    return create_resp(Error('1002','BAD_DATA'), 400)

@app.before_request
def before_request():
    try:
        request.headers['ws-siteid']
    except KeyError:
        return create_resp(Error('1003','UN_AUTHORIZED'), 403)