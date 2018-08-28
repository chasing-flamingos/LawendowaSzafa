import unittest
from test.CartTestCase import CartTestCase

def suite():
    suite = unittest.TestSuite()
    suite.addTest(CartTestCase('test_add_to_cart'))
    suite.addTest(CartTestCase('test_add_to_cart_zero_item'))
    suite.addTest(CartTestCase('test_add_to_cart_out_of_stock'))
    suite.addTest(CartTestCase('test_view_cart'))
    suite.addTest(CartTestCase('test_search'))
    suite.addTest(CartTestCase('test_remove_item_from_cart'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
