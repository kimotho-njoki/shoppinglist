import re

class UpdateLists(object):
    def __init__(self):
        self.all_catalogs = {"grocery":["meat","fruits"], "cloths":["shirt","trouser"]}
        
        self.myLists = {}
        
    def create(self, list_name):
        if list_name in self.all_catalogs:
            self.myLists[list_name] = self.all_catalogs[list_name]
            return "Shoppinglist Created Successfully"
        else: 
            return "Catalog Not Found"

    def create_own(self, list_name):
        if re.match("^[a-zA-Z0-9 _]*$", list_name):
            own_items = []
            self.myLists[list_name] = own_items
            return "Own Shoppinglist Created"
        else:
            print "Shopping List Name Invalid"


    def delete(self, list_name):
        if list_name in self.myLists:
            del self.myLists[list_name]
            return "Shoppinglist Successfully Deleted"
        else:
            return "Shoppinglist Not Found. Please Confirm The Name."


    def edit(self, list_name, new_list_name):
        if list_name in self.all_catalogs:
            self.myLists[new_list_name] = self.myLists.pop(list_name)
            return "Shoppinglist Edited Successfully"
        else:
            return "Shoppinglist Not Found"

    def view(self): 
        return "All Shoppinglists Created"

    
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
















