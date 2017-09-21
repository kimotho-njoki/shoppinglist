"""
creation of shoppinglists and items
"""
import re

class UpdateLists(object):
    """
    class for updating and creating shoppinglists
    """
    def __init__(self):
        """
        constructor methods
        """
        self.all_catalogs = {"grocery":["meat", "fruits"], "cloths":["shirt", "trouser"]}
        self.myLists = {}

    def create(self, list_name):
        """
        method for creating shoppinglist by choosing from catalog
        """
        if list_name in self.all_catalogs:
            self.myLists[list_name] = self.all_catalogs[list_name]
            return "Shoppinglist Created Successfully"
        return "Catalog Not Found"

    def create_own(self, list_name):
        """
        method for creating shoppinglist from scratch
        """
        if re.match("^[a-zA-Z0-9 _]*$", list_name):
            own_items = []
            self.myLists[list_name] = own_items
            return "Own Shoppinglist Created"
        return "Shopping List Name Invalid"

    def delete(self, list_name):
        """
        method for deleting shoppinglist
        """
        if list_name in self.myLists:
            del self.myLists[list_name]
            return "Shoppinglist Successfully Deleted"
        return "Shoppinglist Not Found. Please Confirm The Name."

    def edit(self, list_name, new_list_name):
        """
        method for editing shoppinglist name
        """
        if list_name in self.myLists:
            self.myLists[new_list_name] = self.myLists.pop(list_name)
            return "Shoppinglist Edited Successfully"
        return "Shoppinglist Not Found"

    def view(self):
        """
        method for viewing all created shoppinglists
        """
        return "All Shoppinglists Created"

    def viewitem(self):
        """
        method for viewing all items in shoppinglist
        """
        return "All Items Added"

    def additem(self, list_name, item_name):
        """
        method for adding items
        """
        if re.match("^[a-zA-Z0-9 _]*$", item_name):
            if list_name in self.myLists:
                self.myLists[list_name].append(item_name)
                return "Item Added Successfully"
            return "Item Not Added"
        return "Item Name Invalid"

    def deleteitem(self, list_name, itemname):
        """
        method for deleting an item
        """
        if list_name in self.myLists:
            value = self.myLists[list_name].index(itemname)
            del self.myLists[list_name][value]
            return "Item Deleted Successfully"
        return "Item Not Deleted"
