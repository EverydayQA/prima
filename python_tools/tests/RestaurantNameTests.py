#!/usr/bin/python
import unittest
import sys,os
    pwd = os.path.dirname(os.path.realpath(__file__))
    basedir = os.path.join(pwd,'..')
    print basedir
    sys.path.append(basedir)

    from lib import Restaurant

class RestaurantNameTests(unittest.TestCase):

    def setUp(self):
        self.non_string_name = 123
        self.valid_name = 'Italian rest '
        self.non_alpha_name = 'valid ** n'

    def tearDown(self):
        # this is useless - do not know why
        self.non_string_name = None
        self.valid_name = None
        self.non_alpha_name = None

    def test_non_string_name(self):
        self.assertRaises(TypeError,Restaurant.RestaurantName, self.non_string_name)

    def test_valid_name(self):
        self.assertEqual(Restaurant.RestaurantName(self.valid_name).__str__(), 'Italian rest')

    def test_non_alpha_name(self):
        self.assertRaises(ValueError, Restaurant.RestaurantName, self.non_alpha_name)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(RestaurantNameTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

