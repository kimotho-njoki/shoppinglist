from flask import Flask
from app import accounts, createlist 



app = Flask(__name__, instance_relative_config=True)
app.secret_key = "prettysecret"
app.config.from_object('config')
app.config.from_pyfile('config.py')
	

acc_object = accounts.User()
createlist_object = createlist.UpdateLists()


from app import views

