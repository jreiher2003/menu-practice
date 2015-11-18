from menu import db, models
 

restaurant1 = models.Place(name = "Beef O' Brady's")
db.session.add(restaurant1)
db.session.commit()

restaurant2 = models.Place(name = "Johnny Leverocks")
db.session.add(restaurant2)
db.session.commit()

restaurant3 = models.Place(name = "Lock and Key")
db.session.add(restaurant3)
db.session.commit()

print "3 restaurants were added"