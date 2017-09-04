
class UpdateLists:
	def __init__(self):
		#dictionary holds all catalogs, each holds a list with items
		self.all_catalogs = {"grocery":["meat","fruits"], "cloths":["shirt","trouser"]}
		#dictionary of all the users shoppinglists
		self.myLists = {"grocery":["meat","fruits"], "cloths":["shirt","trouser"]}
		
	
    
	def create(self, list_name):
		if list_name in self.all_catalogs:
			self.myLists[list_name] = self.all_catalogs[list_name]
			return "List Created Successfully"
		else: 
			return "Catalog Not Found"

	
	def delete(self, list_name):
		if list_name in self.myLists:
			del self.myLists[list_name]
			return "List Successfully Deleted"
		else:
			return "List Not Found"


	def edit(self, list_name, new_list_name):
		if list_name in self.all_catalogs:
			self.myLists[new_list_name] = self.myLists.pop(list_name)
			return "List Edited Successfully"
		else:
			return "List Not Found"














