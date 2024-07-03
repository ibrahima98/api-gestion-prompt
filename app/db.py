import psycopg2
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            dbname=current_app.config['DATABASE_NAME'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            host=current_app.config['DATABASE_HOST']
        )
    return g.db

def init_app(app):
    app.teardown_appcontext(close_db)

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
