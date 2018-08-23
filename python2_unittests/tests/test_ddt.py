from ddt import file_data
from ddt import ddt
import os
import json
import unittest2
from pprint import pprint


DATA_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(DATA_PATH, 'data')
data_file = os.path.join(DATA_PATH, 'client.json')
nested_json = os.path.join(DATA_PATH, 'nested.json')


@ddt
class TestPages(unittest2.TestCase):

    def setUp(self):
        pass

    @file_data(data_file)
    def test_sort_by_pricey(self, value):
        pass


class TestUsingSubtest(unittest2.TestCase):

    def setUp(self):
        pass

    def test_sort_by_pricey(self):
        data = json.load(open(data_file))
        self.assertEqual(data, [1, 2, 3, 4, 5])
        self.assertTrue(isinstance(data, list))
        for item in data:
            with self.subTest(item=item):
                self.assertTrue(item, msg=item)

    def test_range_subtest(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual((2 * i) % 2, 0)

    def test_range_without_subtest(self):
        for i in range(0, 6):
            self.assertEqual((i * 2) % 2, 0)

    def test_nested_json(self):
        """
        Example of subTest
        """
        data = json.load(open(nested_json))
        pprint(data)
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 3)
        for item in data:
            pprint(data)
            with self.subTest(id=item.get('id', None)):
                self.assertEqual(type(item), dict)
                self.assertEqual(item.keys(), [u'topping', u'name', u'batters', u'ppu', u'type', u'id'])
                self.assertTrue(item.get('id', None) in [u'0001', u'0002', u'0003'])
