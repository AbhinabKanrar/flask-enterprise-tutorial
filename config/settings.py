import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

THREADS_PER_PAGE = 4

CSRF_ENABLED = False

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'postgres',
    'host': 'localhost',
    'port': '5432',
}

SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
SQLALCHEMY_POOL_RECYCLE = 3600
SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_TRACK_MODIFICATIONS = False