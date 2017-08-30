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
		email = request.form['email']
		repassword = request.form['repwd']

		msg = acc_object.register(username, email, password, repassword)

		if msg == "Successfully signed up. You can now LogIn.":
			return render_template('login.html')
		else:
			return render_template('registration.html')
	return render_template('registration.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['pwd']

		msg = acc_object.Login(username, password)

		if msg == "Successfully Logged In":
			return render_template('createlist.html',resp=msg)
		else:
			return render_template('login.html', resp=msg)
	return render_template('login.html')




@app.route('/createlist', methods=['GET','POST'])
@login_required
def createlist():
	if request.method == 'POST':
		list_name = request.form['list_name']

		msg = createlist_object.create(list_name)

		if msg == "List Created Successfully":
			return render_template('createlist.html', repr=msg)
		else:
			return render_template('createlist.html', repr=msg)
	return render_template('createlist.html')


@app.route('/createlist', methods=['GET','POST'])
@login_required
def deletelist():
	if request.method == 'POST':
		list_name = request.form['list_name']

		msg = createlist_object.delete(list_name)

		if msg == "List Deleted":
			return render_template('createlist.html', repr=msg)
		else:
			return render_template('createlist.html', repr=msg)
	return render_template('createlist.html')


@app.route('/createlist', methods=['GET','POST'])
@login_required
def editlist():
	if request.method == 'POST':
		list_name = request.form['list_name']

		msg = createlist_object.edit(list_name)

		if msg == "List Edited":
			return render_template('createlist.html', repr=msg)
		else:
			return render_template('createlist.html', repr=msg)
	return render_template('createlist.html')



