import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = True
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models