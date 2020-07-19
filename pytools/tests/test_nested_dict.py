import unittest
import json
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
        with open(cls.afile, 'r') as fp:
            cls.dfood = json.load(fp)

    def test_file(self):
        self.assertTrue(os.path.isfile(self.afile))

    def test_dfood(self):
        self.assertEqual(self.dfood.keys(), [u'0001', u'0002', u'0003'])

    def test_get(self):
        v = self.nd.get(*['a', 'b', 'c'], **self.d)
        self.assertEqual(v, 'C')
        dc = copy.deepcopy(self.d)
        items = ['a', 'b', 'e']
        dnew = self.nd.set('E', *items, **dc)
        v = self.nd.get(*['a', 'b', 'e'], **dnew)
        self.assertEqual(v, 'E')

    def test_set(self):
        # update the lastdict with new value of the same key
        dcopy = copy.deepcopy(self.dfood)
        dnew = self.nd.set('topless', *['0002', 'topping', '5001', 'type'],  **dcopy)

        value = self.nd.get(*['0002', 'topping', '5001'], **dnew)
        self.assertEqual(value, {'id': '5001', 'type': 'topless'})
        # update the lastdict with new key: value, but not new dict
        dcopy = copy.deepcopy(self.dfood)
        dnew = self.nd.set('5.01', *['0002', 'topping', '5001', 'price'], **dcopy)
        value = self.nd.get(*['0002', 'topping', '5001'], **dnew)
        self.assertEqual(value, {'id': '5001', 'type': u'None', 'price': '5.01'})

    def test_create(self):
        keys = ['a', 'b', 'c']
        value = {u'd': 1}
        d = self.nd.create(value, *keys)
        dnew = {'a': {'b': {'c': {u'd': 1}}}}
        self.assertEqual(d, dnew)

    def test_update(self):
        source = {'hello1': 1}
        overrides = {'hello2': 2}
        d = self.nd.update(overrides, **source)
        self.assertEqual(d, {'hello1': 1, 'hello2': 2})

        # source did not change
        self.assertEqual(set(d.keys()), set(['hello1', 'hello2']))
        self.assertEqual(source.keys(), ['hello1'])

        value = self.nd.get(*['hello2'], **d)
        self.assertEqual(value, 2)

        source = {'hello': 'to_override'}
        overrides = {'hello': 'over'}
        d = self.nd.update(overrides, **source)
        self.assertEqual(d, {'hello': 'over'})

        source = {'hello': {'value': 'to_override', 'no_change': 1}}
        overrides = {'hello': {'value': 'over'}}
        d = self.nd.update(overrides, **source)
        self.assertEqual(d, {'hello': {'value': 'over', 'no_change': 1}})
        value = self.nd.get(*['hello', 'no_change'], **source)
        self.assertEqual(value, 1)

        source = {'hello': {'value': 'to_override', 'no_change': 1}}
        overrides = {'hello': {'value': {}}}
        dnew = self.nd.update(overrides, **source)
        self.assertEqual(dnew, {'hello': {'value': {}, 'no_change': 1}})

        source = {'hello': {'value': {}, 'no_change': 1}}
        overrides = {'hello': {'value': 2}}
        dnew = self.nd.update(overrides, **source)
        self.assertEqual(dnew, {'hello': {'value': 2, 'no_change': 1}})
