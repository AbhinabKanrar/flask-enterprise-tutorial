from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

from app.common.domain.schema.error import Error
from app.common.util.resp_mapper import create_resp


app = Flask(__name__)

app.config.from_object('config.settings')
app.config.from_envvar('FLASK_ENV',silent=True)

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