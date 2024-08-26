from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your_secret_key_here'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/maillogdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from . import views
    app.register_blueprint(views.bp)

    from .cli import register
    register(app)

    return app
