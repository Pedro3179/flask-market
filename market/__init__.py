from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
db= SQLAlchemy(app)

migrate=Migrate(app, db)

from market import routes