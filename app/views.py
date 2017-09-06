from flask import render_template, request, session, url_for, flash, redirect
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
			flash("Successfully signed up. You can now LogIn.")
			return render_template('login.html')
		else:
			flash("Registration Not Successful. Please Sign Up Again")
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
			flash("Successfully Logged In")
			return render_template('createlist.html')
		else:
			flash("LogIn Unsuccessfull. Please Confirm Details.")
			return render_template('login.html')
	else:
		return render_template('login.html')


@app.route('/create', methods=['GET', 'POST'])
def create_default_list():
	"""
	Create shopping list from catalog
	"""

	default_lists = createlist_object.all_catalogs

	if request.method == 'POST':
		select_value = request.form.get('catalog')

		msg = createlist_object.create(select_value)

		if msg == "List Created Successfully":
			flash("Shoppinglist Created Successfully")
			return render_template('view.html', userlists=createlist_object.myLists)
			
	return render_template('create.html', default_lists=default_lists)
		

@app.route('/delete', methods=['GET','POST'])
def deletelist():
	if request.method == 'POST':
		list_name = request.form['list_name']

		msg = createlist_object.delete(list_name)

		if msg == "List Successfully Deleted":
			flash("Shoppinglist Deleted Successfully")
			return render_template('view.html', userlists=createlist_object.myLists)
		else:
			flash("Shoppinglist Yet To Be Deleted")
			return render_template('delete.html')
	else:
		return render_template('delete.html')


@app.route('/edit', methods=['GET','POST'])
def editlist():
	if request.method == 'POST':
		list_name = request.form['list_name']
		new_list_name = request.form["new_list_name"]

		msg = createlist_object.edit(list_name, new_list_name)

		if msg == "List Edited Successfully":
			flash("Shoppinglist Edited Successfully")
			return render_template('view.html', userlists=createlist_object.myLists)
		else:
			flash("Shoppinglist Editing Failed")
			return render_template('edit.html')
	else:
		return render_template('edit.html')



@app.route('/view', methods=['GET','POST'])
def viewlist():

	msg = createlist_object.view()
	
	if msg == "All Lists Created":
		return render_template('view.html', userlists=createlist_object.myLists)
	else:
		return render_template('createlist.html')




@app.route('/viewitem/<list_name>', methods=['GET','POST'])
def viewitem(list_name):

	msg = createlist_object.viewitem()

	for key in createlist_object.myLists.iterkeys():
		if key == list_name:
			list_items = createlist_object.myLists[key]

	if msg == "All Items Added":
		return render_template('viewitem.html', list_items=list_items, list_name=list_name)
	else:
		return render_template('createlist.html')


@app.route('/additem/<list_name>', methods=['GET','POST'])
def itemadd(list_name):
	if request.method == 'POST':

		itemname = request.form["itemname"]

		msg = createlist_object.additem(list_name, itemname)

		if msg == "Item Added Successfully":
			flash("Item Added Successfully")
			userlists=createlist_object.myLists
			return render_template('view.html', userlists=userlists)
		else:
			flash("Item Adding Failed. Please Try Again.")
			return redirect(url_for('viewitem'))
	else:
		return render_template('additem.html', list_name=list_name)


@app.route('/deleteitem/<list_name>/<item_name>', methods=['POST'])
def itemdel(list_name, item_name):
	if request.method == 'POST':

		msg = createlist_object.deleteitem(list_name, item_name)

		if msg == "Item Deleted Successfully":
			flash("Item Deleted Successfully")
			return render_template('view.html', userlists=createlist_object.myLists)
		else:
			flash("Item Not Deleted. Please Try Again.")
			return redirect(url_for('view.html'))
		


@app.route('/createown', methods=['GET','POST'])
def createownlist():
	if request.method == 'POST':
		list_name = request.form['list_name']

		msg = createlist_object.create_own(list_name)

		if msg == "Own List Created":
			flash("Own Shoppinglist Created Successfully")
			userlists=createlist_object.myLists
			return render_template('view.html', userlists=userlists)
		else:
			flash("Shoppinglist Yet To Be Created")
			return render_template('createown.html')
	else:
		return render_template('createown.html')


	

@app.route('/logout')
def logout():
	flash("You Are Now Logged Out. Come Again.")
	return render_template("index.html")

