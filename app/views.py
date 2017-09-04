from flask import render_template, request, session, url_for
from functools import wraps
from app import app, acc_object, createlist_object

#custom decorator
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
	else:
		return render_template('registration.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['pwd']

		msg = acc_object.LogIn(username, password)

		if msg == "Successfully Logged In":
			session['username'] = username
			return render_template('createlist.html')
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')




@app.route('/create', methods=['GET','POST'])
def createlist():
	if request.method == 'POST':
		list_name = request.form['list_name']

		msg = createlist_object.create(list_name)

		if msg == "List Created Successfully":
			return render_template('additem.html')
		else:
			return render_template('create.html')
	else:
		return render_template('create.html')



@app.route('/delete', methods=['GET','POST'])
def deletelist():
	if request.method == 'POST':
		list_name = request.form['list_name']

		msg = createlist_object.delete(list_name)
		print msg

		if msg == "List Successfully Deleted":
			return render_template('createlist.html')
		else:
			return render_template('delete.html')
	else:
		return render_template('delete.html')


@app.route('/edit', methods=['GET','POST'])
def editlist():
	if request.method == 'POST':
		list_name = request.form['list_name']
		new_list_name = request.form["new_list_name"]

		msg = createlist_object.edit(list_name, new_list_name)
		print msg

		if msg == "List Edited Successfully":
			return render_template('createlist.html')
		else:
			return render_template('edit.html')
	else:
		return render_template('edit.html')


	

@app.route('/logout')
def logout():
	session.pop('username', None)
	return render_template("index.html")

