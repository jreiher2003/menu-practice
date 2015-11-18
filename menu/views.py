from flask import render_template
from menu import app, db
from models import Place, MenuItem

@app.route('/')
@app.route('/place/<int:place_id>/')
def index(place_id):
    place = db.session.query(Place).filter_by(id = place_id).one()
    items = db.session.query(MenuItem).filter_by(place_id=place_id)
    return render_template('base.html', place=place, items=items)
