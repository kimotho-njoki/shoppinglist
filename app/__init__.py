from flask import Flask
from app import accounts, createlist 

from config import app_config

#initialize the app

app = Flask(__name__, instance_relative_config=True)
	
acc_object = accounts.User()
createlist_object = createlist.UpdateLists()

from app import views

app.config.from_object('config')