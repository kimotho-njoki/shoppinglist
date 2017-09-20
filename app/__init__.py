from flask import Flask
from app import accounts, updatelist 

app = Flask(__name__, instance_relative_config=True)
app.secret_key = "prettysecret"
app.debug = True
    
acc_object = accounts.User()
createlist_object = updatelist.UpdateLists()

from app import views
 