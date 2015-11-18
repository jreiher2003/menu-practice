from flask import render_template
from menu import app, db
from models import Place


# from sqlachemy import create_engine 
# from sqlalchemy.orm import sessionmaker
# from models import Base, Place

# engine = create_engine('sqlite:///menu.db')
# Base.metadata.bind = engine 


@app.route('/')
@app.route('/hello')
def index():
    place = db.session.query(Place).all()
    return render_template('base.html', place=place)
