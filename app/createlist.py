import re

class UpdateLists:
	def __init__(self):
		#dictionary holds all catalogs, each holds a list
		self.all_catalogs = {}
		#dictionary of all the users shoppinglists
		self.username = {}
		
	
    
	def create(self, list_name):
		
		for items in self.all_catalogs.iterkeys():
			searchObj = re.search("list_name", self.all_catalogs)
			if searchObj:
				self.username[searchObj.group()] = self.all_catalogs[searchObj.group()]
				return "List Created Successfully"
			else:
				return "No such catalog"

	def delete(self, list_name):
		for items in self.username.iterkeys():
			searchObj = re.search("list_name", self.username)
			if searchObj:
				del(self.username[searchObj.group()])
				return "List Deleted"
			else:
				return "No such catalog"

	def edit(self, list_name):
		new_values = []
		for items in self.username.iterkeys():
			searchObj = re.search("list_name", self.username)
			if searchObj:
				self.username[searchObj.group()] = new_values
				return "List Edited"
			else:
				return "No such catalog"













