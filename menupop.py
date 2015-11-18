from menu import db, models
# from models import MenuItem

place1 = models.Place(name = "Beef O' Brady's")
db.session.add(place1)
db.session.commit()

menuItem8 = models.MenuItem(name = "Veggie Burger", description = "Juicy grilled veggie patty with tomato mayo and lettuce", price = "$7.50", course = "Entree", place = place1)
db.session.add(menuItem8)
db.session.commit()

menuItem1 = models.MenuItem(name = "French Fries", description = "with garlic and parmesan", price = "$2.99", course = "Appetizer", place = place1)
db.session.add(menuItem1)
db.session.commit()

menuItem2 = models.MenuItem(name = "Chicken Burger", description = "Juicy grilled chicken patty with tomato mayo and lettuce", price = "$5.50", course = "Entree", place = place1)
db.session.add(menuItem2)
db.session.commit()

menuItem3 = models.MenuItem(name = "Chocolate Cake", description = "fresh baked and served with ice cream", price = "$3.99", course = "Dessert", place = place1)
db.session.add(menuItem3)
db.session.commit()

menuItem4 = models.MenuItem(name = "Sirloin Burger", description = "Made with grade A beef", price = "$7.99", course = "Entree", place = place1)
db.session.add(menuItem4)
db.session.commit()

menuItem5 = models.MenuItem(name = "Root Beer", description = "16oz of refreshing goodness", price = "$1.99", course = "Beverage", place = place1)
db.session.add(menuItem5)
db.session.commit()

menuItem6 = models.MenuItem(name = "Iced Tea", description = "with Lemon", price = "$.99", course = "Beverage", place = place1)
db.session.add(menuItem6)
db.session.commit()

menuItem7 = models.MenuItem(name = "Grilled Cheese Sandwich", description = "On texas toast with American Cheese", price = "$3.49", course = "Entree", place = place1)
db.session.add(menuItem7)
db.session.commit()
########################################################
########################################################
place2 = models.Place(name = "Johnny Leverocks")
db.session.add(place2)
db.session.commit()

menuItem1 = models.MenuItem(name = "Chicken Stir Fry", description = "With your choice of noodles vegetables and sauces", price = "$7.99", course = "Entree", place = place2)
db.session.add(menuItem1)
db.session.commit()

menuItem2 = models.MenuItem(name = "Peking Duck", description = " A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price = "$25", course = "Entree", place = place2)
db.session.add(menuItem2)
db.session.commit()

menuItem3 = models.MenuItem(name = "Spicy Tuna Roll", description = "Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ", price = "15", course = "Entree", place = place2)
db.session.add(menuItem3)
db.session.commit()

menuItem4 = models.MenuItem(name = "Nepali Momo ", description = "Steamed dumplings made with vegetables, spices and meat. ", price = "12", course = "Entree", place = place2)
db.session.add(menuItem4)
db.session.commit()

menuItem5 = models.MenuItem(name = "Beef Noodle Soup", description = "A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.", price = "14", course = "Entree", place = place2)
db.session.add(menuItem5)
db.session.commit()

menuItem6 = models.MenuItem(name = "Ramen", description = "a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.", price = "12", course = "Entree", place = place2)
db.session.add(menuItem6)
db.session.commit()

########################################################
########################################################
place3 = models.Place(name = "Lock and Key")
db.session.add(place3)
db.session.commit()

menuItem1 = models.MenuItem(name = "Pho", description = "a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.", price = "$8.99", course = "Entree", place = place3)
db.session.add(menuItem1)
db.session.commit()

menuItem2 = models.MenuItem(name = "Chinese Dumplings", description = "a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.", price = "$6.99", course = "Appetizer", place = place3)
db.session.add(menuItem2)
db.session.commit()

menuItem3 = models.MenuItem(name = "Gyoza", description = "The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner", price = "$9.95", course = "Entree", place = place3)
db.session.add(menuItem3)
db.session.commit()

menuItem4 = models.MenuItem(name = "Stinky Tofu", description = "Taiwanese dish, deep fried fermented tofu served with pickled cabbage.", price = "$6.99", course = "Entree", place = place3)
db.session.add(menuItem4)
db.session.commit()

menuItem5 = models.MenuItem(name = "Veggie Burger", description = "Juicy grilled veggie patty with tomato mayo and lettuce", price = "$9.50", course = "Entree", place = place3)
db.session.add(menuItem5)
db.session.commit()


print "3 restaurants were added"
print "menu items were added"