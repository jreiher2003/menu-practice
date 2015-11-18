from flask import render_template
from menu import app, db
from models import Place, MenuItem

@app.route('/')
@app.route('/hello')
def index():
    place = db.session.query(Place).all()
    items = db.session.query(Place,MenuItem).filter(Place.id==MenuItem.place_id).all()
    return render_template('base.html', place=place, items=items)
