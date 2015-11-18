#!flask/bin/python
from config import SQLALCHEMY_DATABASE_URI
from menu import db

db.create_all()
