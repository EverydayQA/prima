import unittest
import os
import copy
from nested.nested_dict import NestedDict


class TestNestedDict(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        path = os.path.dirname(__file__)
        cls.afile = os.path.join(path, '../nested/data/food_nested_dict.json')
        cls.nd = NestedDict()
        cls.d = {'a': {'b': {'c': 'C'}}}

    def test_file(self):
        self.assertTrue(os.path.isfile(self.afile))

    def test_get(self):
        v = self.nd.get(self.d, ['a', 'b', 'c'])
        self.assertEqual(v, 'C')
        dc = copy.deepcopy(self.d)
        items = ['a', 'b', 'e']
        d = self.nd.set(items, 'E', **dc)
        v = self.nd.get(d, ['a', 'b', 'e'])
        self.assertEqual(v, 'E')

    def test_update(self):
        source = {'hello1': 1}
        overrides = {'hello2': 2}
        d = self.nd.update(source, overrides)
        self.assertEqual(source, {'hello1': 1, 'hello2': 2})
        self.assertEqual(d, source)
        value = self.nd.get(d, ['hello2'])
        self.assertEqual(value, 2)

        source = {'hello': 'to_override'}
        overrides = {'hello': 'over'}
        self.nd.update(source, overrides)
        self.assertEqual(source, {'hello': 'over'})

        source = {'hello': {'value': 'to_override', 'no_change': 1}}
        overrides = {'hello': {'value': 'over'}}
        self.nd.update(source, overrides)
        self.assertEqual(source, {'hello': {'value': 'over', 'no_change': 1}})
        value = self.nd.get(source, ['hello', 'no_change'])
        self.assertEqual(value, 1)

        source = {'hello': {'value': 'to_override', 'no_change': 1}}
        overrides = {'hello': {'value': {}}}
        self.nd.update(source, overrides)
        self.assertEqual(source, {'hello': {'value': {}, 'no_change': 1}})

        source = {'hello': {'value': {}, 'no_change': 1}}
        overrides = {'hello': {'value': 2}}
        self.nd.update(source, overrides)
        self.assertEqual(source, {'hello': {'value': 2, 'no_change': 1}})
