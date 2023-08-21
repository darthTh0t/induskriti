from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from app import routes

app.config["SECRET_KEY"] = "62703beee209986fac2964d06d60e0be"
