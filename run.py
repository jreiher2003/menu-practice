#!flask/bin/python
from menu import app
app.secret_key = 'super_secret_key'
app.debug = True
app.run(host="localhost", port=5005)