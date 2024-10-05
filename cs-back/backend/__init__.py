from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail
# from celery.schedules import crontab
from flask_caching import Cache
app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_campus.sqlite3'  # using SQLite for simplicity
# sqlite:///kanaban.sqlite3

jwt = JWTManager(app)
db = SQLAlchemy(app)
api = Api(app)
CORS(app, methods=["GET", "POST", "PUT", "DELETE"])

from backend import routes
