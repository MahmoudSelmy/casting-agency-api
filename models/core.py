import os

from flask_sqlalchemy import SQLAlchemy

database_path = os.environ.get('DATABASE_URL', 'postgresql://pc@localhost:5432/agency')

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
