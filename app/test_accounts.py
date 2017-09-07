import unittest
from accounts import User

class TestAccounts(unittest.TestCase):
	"""
	Test for LogIn with account
	Test for LogIn with no account
	Test for LogIn with incorrect password
	Test for successfull Sign Up
	Test for registering with an already existing username
	Test for too short password
	"""
	def setUp(self):
		self.account_object = User()
	
	def tearDown(self):
		del self.account_object


	def test_success_LogIn(self):
		result = self.account_object.LogIn('grace', 'welcome')
		self.assertEqual(result, "Successfully Logged In")

	def test_failed_LogIn(self):
		result = self.account_object.LogIn('betty', 'beatrice')
		self.assertEqual(result, "Account does not exist. Please Register.")

	def test_incorrect_pwd(self):
		result = self.account_object.LogIn('grace', 'emphasis')
		self.assertEqual(result, "Incorrect Password")

	def test_success_registration(self):
		result = self.account_object.Register('john', 'john@gmail.com', 'johnjohn', 'johnjohn')
		self.assertEqual(result, "Successfully signed up. You can now LogIn.")

	def test_rpt_username(self):
		result = self.account_object.Register('grace', 'grayce@gmail.com', 'kimotho', 'kimotho')
		self.assertEqual(result, "Username already exists")

	def test_short_pwd(self):
		result = self.account_object.Register('hanah', 'hanah@gmail.com', 'hey', 'hey')
		self.assertEqual(result, "Password Invalid")

if __name__ == '__main__':
	unittest.main()
