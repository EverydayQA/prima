import os
import unittest
from pprint import pprint
import json
from src.parse_file import DPaseFile


class TestDPaseFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        path = os.path.dirname(__file__)
        cls.afile = os.path.join(path, '../data/dump.txt')
        cls.pd = DPaseFile(cls.afile)
        cls.d = cls.pd.df

    def test_d_deep_get(self):
        pprint(self.d)
        v = self.pd.d_deep_get(self.d, 'variables.acquisition.window_widthx', 1000)
        print(v)
        self.assertEqual(v, 1000)

    def test_deep_update(self):
        source = {'hello1': 1}
        overrides = {'hello2': 2}
        self.pd.d_update(source, overrides)
        self.assertEqual(source, {'hello1': 1, 'hello2': 2})

        source = {'hello': 'to_override'}
        overrides = {'hello': 'over'}
        self.pd.d_update(source, overrides)
        self.assertEqual(source, {'hello': 'over'})

        source = {'hello': {'value': 'to_override', 'no_change': 1}}
        overrides = {'hello': {'value': 'over'}}
        self.pd.d_update(source, overrides)
        self.assertEqual(source, {'hello': {'value': 'over', 'no_change': 1}})

        source = {'hello': {'value': 'to_override', 'no_change': 1}}
        overrides = {'hello': {'value': {}}}
        self.pd.d_update(source, overrides)
        self.assertEqual(source, {'hello': {'value': {}, 'no_change': 1}})

        source = {'hello': {'value': {}, 'no_change': 1}}
        overrides = {'hello': {'value': 2}}
        self.pd.d_update(source, overrides)
        self.assertEqual(source, {'hello': {'value': 2, 'no_change': 1}})

    def test_dict_to_json(self):
        """
        """
        self.assertTrue(isinstance(self.d, dict))
        # json.dumps() converts a dictionary to str object,
        json_file = json.dumps(self.d)
        self.assertTrue(isinstance(json_file, str))
        # Output str
        print(type(json_file))

        # so you have to load your str into a dict to use it by using json.loads() method
        json_obj = json.loads(json_file)
        # equal to initial dict
        self.assertEqual(json_obj, self.d)
        pprint(json_obj)

        self.assertTrue(isinstance(json_obj, dict))
        self.assertFalse('listName' in json_obj)
