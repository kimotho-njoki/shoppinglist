import re

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

	def create_own(self, list_name):
		if re.match("^[a-zA-Z0-9 _]*$", list_name):
			own_items = []
			self.myLists[list_name] = own_items
			return "Own List Created"
		else:
			print "Shopping List Name Invalid"


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

	def view(self): 
		return "All Lists Created"

	def viewitem(self):
		return "All Items Added"

	def additem(self, list_name, item_name):
		if re.match("^[a-zA-Z0-9 _]*$", item_name):
			if list_name in self.myLists:
				self.myLists[list_name].append(item_name)
				return "Item Added Successfully"
			else:
				return "Item Not Added"
		else:
			return "Item Name Invalid"

	def deleteitem(self, list_name, itemname):
		if list_name in self.myLists:
			value = self.myLists[list_name].index(itemname)
			del self.myLists[list_name][value]
			return "Item Deleted Successfully"
		else:
			return "Item Not Deleted"
















