import unittest
import os
import copy
from src.nested_dict import NestedDict


class TestNestedDict(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        path = os.path.dirname(__file__)
        cls.afile = os.path.join(path, 'data/dump.txt')
        cls.nd = NestedDict()
        cls.d = {'a': {'b': {'c': 'C'}}}

    def test_deep_get(self):
        d = self.nd.deep_get(self.d, ['a', 'b', 'c'])
        self.assertEqual(d, 'C')

    def test_d_deep_get(self):
        v = self.nd.d_deep_get(self.d, ['a', 'b', 'c'], default='NA')
        self.assertEqual(v, 'C')
        dc = copy.deepcopy(self.d)
        d = self.nd.deep_set(dc, 'E', ['a', 'b', 'e'])
        v = self.nd.d_deep_get(d, ['a', 'b', 'e'], default='NA')
        self.assertEqual(v, 'E')

    def test_deep_update(self):
        source = {'hello1': 1}
        overrides = {'hello2': 2}
        self.nd.deep_update(source, overrides)
        self.assertEqual(source, {'hello1': 1, 'hello2': 2})

        source = {'hello': 'to_override'}
        overrides = {'hello': 'over'}
        self.nd.deep_update(source, overrides)
        self.assertEqual(source, {'hello': 'over'})

        source = {'hello': {'value': 'to_override', 'no_change': 1}}
        overrides = {'hello': {'value': 'over'}}
        self.nd.deep_update(source, overrides)
        self.assertEqual(source, {'hello': {'value': 'over', 'no_change': 1}})

        source = {'hello': {'value': 'to_override', 'no_change': 1}}
        overrides = {'hello': {'value': {}}}
        self.nd.deep_update(source, overrides)
        self.assertEqual(source, {'hello': {'value': {}, 'no_change': 1}})

        source = {'hello': {'value': {}, 'no_change': 1}}
        overrides = {'hello': {'value': 2}}
        self.nd.deep_update(source, overrides)
        self.assertEqual(source, {'hello': {'value': 2, 'no_change': 1}})
