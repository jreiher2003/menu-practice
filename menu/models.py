from menu import db

class Place(db.Model):
    __tablename__ = 'place' # names table
    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Place %r>' % (self.name)


class MenuItem(db.Model):
	__tablename__ = 'menuItem'
	name = db.Column(db.String(80), nullable=False)
	id = db.Column(db.Integer, primary_key=True)
	course = db.Column(db.String(250))
	description = db.Column(db.String(250))
	price = db.Column(db.String(8))
	place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
	place = db.relationship(Place)

	def __repr__(self):
		return '<MenuItem %r>' % (self.name)


