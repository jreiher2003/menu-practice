from flask import render_template
from menu import app, db
from models import Place, MenuItem

@app.route('/')
@app.route('/place/<int:place_id>/')
def index(place_id):
    place = db.session.query(Place).filter_by(id = place_id).one()
    items = db.session.query(MenuItem).filter_by(place_id=place_id)
    return render_template('base.html', place=place, items=items)

#task 1: create route for newMenuItem fucntion here
@app.route('/place/<int:place_id>/new/')
def newMenuItem(place_id):
	return "page to create a new menu item. task 1 complete"

@app.route('/place/<int:place_id>/<int:menu_id>/')
def editMenuItem(place_id, menu_id):
	return "page to edit new menu items. task 2 complete"

@app.route('/place/<int:place_id>/<int:menu_id>')
def deleteMenuItem(place_id, menu_id):
	return "page to delete a new menu item. Task 3 complete"
