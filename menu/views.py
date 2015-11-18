from flask import render_template
from menu import app, db
from models import Place

@app.route('/')
@app.route('/hello')
def index():
    place = db.session.query(Place).all()
    return render_template('base.html', place=place)
