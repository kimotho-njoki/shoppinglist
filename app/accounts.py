"""
handles user authentication
"""
import re

class User(object):
    """
    user class for user registration and login
    """
    def __init__(self):
        """
        contructor
        """
        self.user_details = {'grace':'welcome'}
        self.extra_details = {}

    def LogIn(self, username, password):
        """
        method for signing in users
        """
        if username == '':
            return "Username field cannot be empty"
        if username in self.user_details:
            if self.user_details[username] == password:
                return "Successfully Logged In"
            return "Password Either Incorrect Or Empty"
        return "Account does not exist. Please Register."

    def Register(self, username, email, password, repassword):
        """
        method for registering users
        """
        if re.match("^[a-zA-Z0-9 _]*$", username):
            if username in self.user_details:
                return "Username already exists"
            if username == '':
                return "Username field cannot be empty"
            if len(password) < 6 or password != repassword or\
            password == '' or repassword == '':
                return "Password Either Too Short Or Empty"
            self.user_details[username] = password
            self.extra_details[username] = [email, repassword]
            return "Successfully signed up. You can now LogIn."
        return "Username Invalid"
