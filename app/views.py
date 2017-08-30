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
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['pwd']
		print password
		email = request.form['email']
		repassword = request.form['repwd']

		msg = acc_object.register(username, email, password, repassword)
		print msg

		if msg == "Successfully signed up. You can now LogIn.":
			return render_template('login.html')
		else:
			return render_template('registration.html')
	else:
		return render_template('registration.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		print username
		password = request.form['pwd']
		print password

		msg = acc_object.LogIn(username, password)
		print msg

		if msg == "Successfully Logged In":
			return render_template('createlist.html')
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')




@app.route('/createlist', methods=['GET','POST'])
@login_required
def createlist():
	if request.method == 'POST':
		list_name = request.form['list_name']

		msg = createlist_object.create(list_name)

		if msg == "List Created Successfully":
			return render_template('createlist.html')
		else:
			return render_template('createlist.html')
	else:
		return render_template('createlist.html')


@app.route('/createlist', methods=['GET','POST'])
@login_required
def deletelist():
	if request.method == 'POST':
		list_name = request.form['list_name']

		msg = createlist_object.delete(list_name)

		if msg == "List Deleted":
			return render_template('createlist.html')
		else:
			return render_template('createlist.html')
	else:
		return render_template('createlist.html')


@app.route('/createlist', methods=['GET','POST'])
@login_required
def editlist():
	if request.method == 'POST':
		list_name = request.form['list_name']

		msg = createlist_object.edit(list_name)

		if msg == "List Edited":
			return render_template('createlist.html')
		else:
			return render_template('createlist.html')
	else:
		return render_template('createlist.html')



