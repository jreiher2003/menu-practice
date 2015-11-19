from flask import render_template, request, redirect, url_for
from menu import app, db
from models import Place, MenuItem

# read
@app.route('/')
@app.route('/place/<int:place_id>/')
def menu(place_id):
    place = db.session.query(Place).filter_by(id = place_id).one()
    items = db.session.query(MenuItem).filter_by(place_id=place_id)
    return render_template('base.html', place=place, items=items)

# create
@app.route('/place/<int:place_id>/new/', methods=['GET', 'POST'])
def newMenuItem(place_id):
	if request.method == 'POST':
		newItem = MenuItem(name = request.form['name'], price= request.form['price'], place_id=place_id)
		db.session.add(newItem)
		db.session.commit()
		return redirect(url_for('menu',place_id=place_id))

	if request.method == 'GET':
		return render_template('newMenuItem.html', place_id=place_id)

# update
@app.route('/place/<int:place_id>/<int:menu_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(place_id, menu_id):
	placeholder = db.session.query(MenuItem).filter_by(id = menu_id).one()		
	if request.method == 'POST':
		umenu = db.session.query(MenuItem).filter_by(id = menu_id).one()
		umenu.name = request.form['name']
		umenu.price = request.form['price']
		db.session.add(umenu)
		db.session.commit()
		return redirect(url_for('menu', place_id=place_id))

	return render_template('editMenuItem.html', place_id=place_id,menu_id=menu_id,placeholder=placeholder)

# delete
@app.route('/place/<int:place_id>/<int:menu_id>/delete/')
def deleteMenuItem(place_id, menu_id):
	return "page to delete a new menu item. Task 3 complete"
