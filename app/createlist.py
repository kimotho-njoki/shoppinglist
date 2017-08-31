
class UpdateLists:
	def __init__(self):
		#dictionary holds all catalogs, each holds a list with items
		self.all_catalogs = {}
		#dictionary of all the users shoppinglists
		self.myLists = {}
		
	
    
	def create(self, list_name):
		if list_name in self.all_catalogs:
			self.myLists[list_name] = self.all_catalogs[list_name]
			return "List Created Successfully"
		else:
			return "Catalog Not Found"

	
	def delete(self, list_name):
		if list_name in self.myLists:
			del myLists[list_name]
			return "List Successfully Deleted"
		else:
			return "List Not Found"


	def edit(self, list_name):
		new_items = []
		if list_name in self.all_catalogs:
			self.myLists.get(list_name) and self.myLists.update({list_name:new_items})
			return "List Edited Successfully"
		else:
			return "List Not Found"













