# from markupsafe import Markup
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_googlemaps import GoogleMaps

# class Base(DeclarativeBase):
#   pass

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
# app.config['GOOGLEMAPS_KEY'] = "AIzaSyAnxATYjE527zrolA4D2krAmZpGC_3Zl_o"
db.init_app(app)

GoogleMaps(app, key="AIzaSyAnxATYjE527zrolA4D2krAmZpGC_3Zl_o")

from .models import Enda
with app.app_context():
    db.create_all()
    from .data import *

import wateraware.views