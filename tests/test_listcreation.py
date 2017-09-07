"""
shoppinglist creation tests
"""
import unittest
from app.updatelist import UpdateLists

class TestLists(unittest.TestCase):
    """
    Test if list_name in all_catalogs
    Test if list_name not in all_catalogs
    Test invalid list_name
    Test correct list_name
    """

    def setUp(self):
        """
        initialize object
        """
        self.shoplist = UpdateLists()

    def tearDown(self):
        """
        delete object
        """
        del self.shoplist

    def test_namein_catalog(self):
        """
        tests creating shoppinglist from catalog
        """
        result = self.shoplist.create("grocery")
        self.assertEqual(result, "Shoppinglist Created Successfully")

    def test_notin_catalog(self):
        """
        tests trying to create a shoppinglist from catalog that doesn't exist
        """
        result = self.shoplist.create("bags")
        self.assertEqual(result, "Catalog Not Found")

    def test_invalid_name(self):
        """
        tests the use of unauthorized characters in shoppinglist name
        """
        result = self.shoplist.create_own(".#")
        self.assertEqual(result, None)

    def test_correct_name(self):
        """
        tests the use of correct characters in shoppinglist name
        """
        result = self.shoplist.create_own("soaps")
        self.assertEqual(result, "Own Shoppinglist Created")

if __name__ == '__main__':
    unittest.main()
