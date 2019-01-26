#!/usr/bin/python
import unittest
from python2_unittests.fsample.restaurant import RestaurantName


class TestRestaurantName(unittest.TestCase):

    def setUp(self):
        self.non_string_name = 123
        self.valid_name = 'Italianrest123'
        self.non_alpha_name = 'valid **\n'

    def tearDown(self):
        # this is useless - do not know why
        self.non_string_name = None
        self.valid_name = None
        self.non_alpha_name = None

    def test_non_string_name(self):
        with self.assertRaises(TypeError):
            RestaurantName(self.non_string_name)

    def test_valid_name(self):
        with self.assertRaises(ValueError):
            RestaurantName(self.valid_name)

    def test_non_alpha_name(self):
        with self.assertRaises(TypeError):
            RestaurantName(self.non_alpha_name)
