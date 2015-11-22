from flask import render_template, request, redirect, url_for, flash
from menu import app, db
from models import Place, MenuItem

@app.route('/base/')
def base():
	return render_template('base.html')
# read
@app.route('/')
def place():
	places = db.session.query(Place).all()
	return render_template('place.html', places=places)

@app.route('/newplace/', methods=["GET", "POST"])
def newPlace():
	if request.method == 'POST':
		newplace = Place(name = request.form['name'])
		db.session.add(newplace)
		db.session.commit()
		flash('New Restaurant Created!')
		return redirect(url_for('place'))
	return render_template('newPlace.html')

@app.route('/place/<int:place_id>/edit/', methods=["GET", "POST"])
def editPlace(place_id):
	place = db.session.query(Place).filter_by(id = place_id).one()
	if request.method == "POST":
		# editPlace = db.session.query(Place).filter_by(id = place_id).one()
		place.name = request.form['name']
		db.session.add(place)
		db.session.commit()
		flash('succesfully edited a Restaurant name!')
		return redirect(url_for('menu', place_id=place_id))

	return render_template('editPlace.html', place_id=place_id, place=place)

@app.route('/place/<int:place_id>/delete/', methods=["GET", "POST"])
def deletePlace(place_id):
	delplace = db.session.query(Place).filter_by(id=place_id).one()
	if request.method == 'POST':
		db.session.delete(delplace)
		db.session.commit()
		flash('succesfully deleted a Restaurant!')
		return redirect(url_for('place'))

	
	if request.method == 'GET':
		return render_template('deletePlace.html', place_id=place_id, delplace=delplace)

@app.route('/place/<int:place_id>/')
def menu(place_id):
    place = db.session.query(Place).filter_by(id = place_id).one()
    items = db.session.query(MenuItem).filter_by(place_id=place_id)
    return render_template('menu.html', place=place, items=items)

# create
@app.route('/place/<int:place_id>/new/', methods=['GET', 'POST'])
def newMenuItem(place_id):
	if request.method == 'POST':
		newItem = MenuItem(name = request.form['name'], price= request.form['price'], place_id=place_id)
		db.session.add(newItem)
		db.session.commit()
		flash("new menu item created!")
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
		flash("menu item succesfully edited")
		return redirect(url_for('menu', place_id=place_id))

	return render_template('editMenuItem.html', place_id=place_id,menu_id=menu_id,i=placeholder)

# delete
@app.route('/place/<int:place_id>/<int:menu_id>/delete/', methods=["GET", "POST"])
def deleteMenuItem(place_id, menu_id):
	delmenu = db.session.query(MenuItem).filter_by(id = menu_id).one()
	if request.method == 'POST':
		db.session.delete(delmenu)
		db.session.commit()
		flash("menu item succesfully deleted")
		return redirect(url_for('menu', place_id=place_id))

	return render_template('deleteMenuItem.html', place_id=place_id, menu_id=menu_id, i=delmenu)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404