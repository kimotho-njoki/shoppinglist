import re

class User:
    def __init__(self):
        self.user_details = {'grace':'welcome'}
        self.extra_details = {}

    def LogIn(self, username, password):
        if username in self.user_details:
            if self.user_details[username] == password:
                return "Successfully Logged In"
            else:
                return "Incorrect Password"
        else:
            return "Account does not exist. Please Register."	
    def Register(self, username, email, password, repassword):
        if re.match("^[a-zA-Z0-9 _]*$", username):
			if username in self.user_details:
				return "Username already exists"
			else:
				if len(password) < 6 or password != repassword or password == '' or repassword == '':
					return "Password Invalid"
				else:
					self.user_details[username] = password
					self.extra_details[username] = [email, repassword]
					return "Successfully signed up. You can now LogIn."
        else:
			return "Username Invalid"
