"""
defining routes
"""
from flask import render_template, request, session, url_for, flash, redirect
from functools import wraps
from app import app, acc_object, createlist_object

def login_required(f):
    """
    custom decorator
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        """
        custom decorator to ensure user is logged in to view pages
        """
        if "username" in session:
            return f(*args, **kwargs)
        msg = "You are not logged in"
        return render_template('index.html', resp=msg)
    return decorated_function

@app.route('/')
def home():
    """
    redirects user to the home page
    """
    return render_template('index.html')

@app.route('/registration', methods=['GET', 'POST'])
def register():
    """
    redirects user to the registration page
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pwd']
        email = request.form['email']
        repassword = request.form['repwd']

        msg = acc_object.Register(username, email, password, repassword)

        if msg == "Successfully signed up. You can now LogIn.":
            flash("Successfully signed up. You can now LogIn.")
            return render_template('login.html')
        flash(msg, "error")
        return render_template('registration.html')
    return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    redirects the user to the login page
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pwd']

        msg = acc_object.LogIn(username, password)

        if msg == "Successfully Logged In":
            flash("Successfully Logged In")
            return render_template('createlist.html')
        flash(msg, "error")
        return render_template('login.html')
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

        if msg == "Shoppinglist Created Successfully":
            flash("Shoppinglist Created Successfully")
            return render_template('view.html', userlists=createlist_object.myLists)
    return render_template('create.html', default_lists=default_lists)

@app.route('/delete', methods=['GET', 'POST'])
def deletelist():
    """
    redirects user to the viewing page after deletion is complete
    """
    if request.method == 'POST':
        list_name = request.form['list_name']

        msg = createlist_object.delete(list_name)

        if msg == "Shoppinglist Successfully Deleted":
            flash("Shoppinglist Deleted Successfully")
            return render_template('view.html', userlists=createlist_object.myLists)
        flash("Shoppinglist Yet To Be Deleted. Please input the correct shoppinglist name."\
            , "error")
        return render_template('viewitem.html')
    return render_template('viewitem.html')

@app.route('/edit', methods=['GET', 'POST'])
def editlist():
    """
    redirects user to the viewing page after editing is complete
    """
    if request.method == 'POST':
        list_name = request.form['list_name']
        new_list_name = request.form["new_list_name"]

        msg = createlist_object.edit(list_name, new_list_name)

        if msg == "Shoppinglist Edited Successfully":
            flash("Shoppinglist Edited Successfully")
            return render_template('view.html', userlists=createlist_object.myLists)
        flash("Shoppinglist Editing Failed. \
            PLease input the correct shoppinglist name and do not use \
            special characters in the new name.", "error")
        return render_template('edit.html')
    return render_template('edit.html')

@app.route('/view', methods=['GET', 'POST'])
def viewlist():
    """
    redirects user to the viewing page
    """
    msg = createlist_object.view()
    if msg == "All Shoppinglists Created":
        return render_template('view.html', userlists=createlist_object.myLists)
    return render_template('createlist.html')

@app.route('/viewitem/<list_name>', methods=['GET', 'POST'])
def viewitem(list_name):
    """
    redirects user to view all items added to shoppinglist
    """

    msg = createlist_object.viewitem()

    for key in createlist_object.myLists.iterkeys():
        if key == list_name:
            list_items = createlist_object.myLists[key]

    if msg == "All Items Added":
        return render_template('viewitem.html', list_items=list_items, list_name=list_name)
    return render_template('createlist.html')

@app.route('/additem/<list_name>', methods=['GET', 'POST'])
def itemadd(list_name):
    """
    redirects user to the viewing page after adding items
    """
    if request.method == 'POST':

        itemname = request.form["itemname"]

        msg = createlist_object.additem(list_name, itemname)

        if msg == "Item Added Successfully":
            flash("Item Added Successfully")
            userlists = createlist_object.myLists
            return render_template('view.html', userlists=userlists)
        flash("Item Adding Failed. Please try again \
            and do not add any special characters to the name.", "error")
        return redirect(url_for('viewitem'))
    return render_template('additem.html', list_name=list_name)

@app.route('/deleteitem/<list_name>/<item_name>', methods=['POST'])
def itemdel(list_name, item_name):
    """
    redirects user to the viewing page after item deletion is complete
    """
    if request.method == 'POST':

        msg = createlist_object.deleteitem(list_name, item_name)

        if msg == "Item Deleted Successfully":
            flash("Item Deleted Successfully")
            return render_template('view.html', userlists=createlist_object.myLists)
        flash("Item Not Deleted. Please Try Again.", "error")
        return redirect(url_for('view.html'))

@app.route('/createown', methods=['GET', 'POST'])
def createownlist():
    """
    redirects user to the viewing page after creating a shoppinglist from the catalog
    """
    if request.method == 'POST':
        list_name = request.form['list_name']

        msg = createlist_object.create_own(list_name)

        if msg == "Own Shoppinglist Created":
            flash("Own Shoppinglist Created Successfully")
            userlists = createlist_object.myLists
            return render_template('view.html', userlists=userlists)
        flash("Shoppinglist Yet To Be Created. \
            Please try again and do not include any \
            special characters in the shoppinglist name.", "error")
        return render_template('createown.html')
    return render_template('createown.html')

@app.route('/logout')
def logout():
    """
    redirects user to the home page after logging out
    """
    flash("You Are Now Logged Out. Come Again.")
    return render_template("index.html")
