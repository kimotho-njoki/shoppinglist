class User:
	def __init__(self):
		self.user_details = {}

	def LogIn(self, username, password):
		for usernm in self.user_details.iterkeys():
			if username == usernm['username']:
				for passwd in self.user_details.itervalues():
					if password == passwd['password']:
						return "Successfully Logged In"
					else:
						return "Incorrect password"
			else:
				return "Incorrect username, if not registered please register"

	def register(self, username, email, password, repassword):
		
		for user in self.user_details.iterkeys():
			if username == user['username']:
				return "Username already exists"
			else:
				if len(password) < 8:
					return "Password too short"
				else:
					self.user_details[username] = password
					return "Successfully signed up. You can now LogIn."

					
