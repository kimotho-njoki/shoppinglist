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
			return "Account does not exist. Please Register"
		

	def register(self, username, email, password, repassword):
		if username in self.user_details:
			return "Username already exists"
		else:
			if len(password) < 6:
				return "Password too short"
			else:
				self.user_details[username] = password
				self.extra_details[username] = [email, repassword]
				return "Successfully signed up. You can now LogIn."

					
