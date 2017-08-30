from flask import render_template, request, session, url_for
from functools import wraps
from app import app, acc_object, createlist_object


def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if "username" in session:
			return f(*args, **kwargs)
		else:
			msg = "You are not logged in"
			return render_template('index.html', resp=msg)
			
	return decorated_function

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/registration', methods=['GET','POST'])
def register():
	return render_template('registration.html')

@app.route('/lostpwd', methods=['GET','POST'])
@login_required
def password():
	return render_template('lostpwd.html')

@app.route('/lostusernm', methods=['GET','POST'])
@login_required
def username():
	return render_template('lostusernm.html')

@app.route('/createlist', methods=['GET','POST'])
@login_required
def create():
	return render_template('createlist.html')

@app.route('/catalog', methods=['GET','POST'])
@login_required
def catalog():
	return render_template('catalog.html')

@app.route('/mylist1', methods=['GET','POST'])
@login_required
def mylist1():
	return render_template('mylist1.html')

@app.route('/mylist2', methods=['GET','POST'])
@login_required
def mylist2():
	return render_template('mylist2.html')
