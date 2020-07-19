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

    def test_deepset_keys(self):
        # need this key to set
        source = {'hello1': 1}
        keys = self.nd.deepset_keys(**source)
        self.assertEqual(keys, ['hello1'])

        source = {'hello': {'value': 'to_override', 'no_change': 1}}
        keys = self.nd.deepset_keys(**source)
        self.assertEqual(keys, ['hello'])

        source = {'hello': 1, 'h2': 2}
        keys = self.nd.deepset_keys(**source)
        self.assertEqual(keys, [])

    def test_shallow_setstar(self):
        d = {'hello1': 1}
        dnew = self.nd.shallow_setstar('foo', 'FOO', **d)
        self.assertEqual(dnew.get('foo', None), 'FOO')
        self.assertEqual(d.get('foo', None), None)

        self.assertEqual(d.get('hello1', None), 1)
        self.assertEqual(dnew.get('hello1', None), 1)

    def test_shallow_set(self):
        d = {'hello1': 1}
        dnew = self.nd.shallow_set('foo', 'FOO', d)
        self.assertEqual(dnew.get('foo', None), 'FOO')
        self.assertEqual(d.get('foo', None), 'FOO')

        self.assertEqual(d.get('hello1', None), 1)
        self.assertEqual(dnew.get('hello1', None), 1)
        self.assertEqual(d, dnew)

    def test_merge_shallow(self):
        d = {}
        dnew = {}
        du = self.nd.merge_shallow(dnew, **d)
        self.assertEqual(du, d)

        source = {'hello1': 1}
        overrides = {'hello2': 2}
        du = self.nd.merge_shallow(overrides, **source)
        self.assertEqual(du, {'hello1': 1, 'hello2': 2})

        source = {'hello': {'value': 'to_override', 'no_change': 1}}
        overrides = {'hello': {'value': 'over'}}
        d = self.nd.update2(overrides, **source)
        self.assertEqual(d, {'hello': {'value': 'over', 'no_change': 1}})

    def test_update2(self):
        source = {'hello1': 1}
        overrides = {'hello2': 2}
        d = self.nd.update2(overrides, **source)
        self.assertEqual(d, {'hello1': 1, 'hello2': 2})

        # source did not change
        self.assertEqual(set(d.keys()), set(['hello1', 'hello2']))
        self.assertEqual(source.keys(), ['hello1'])

        value = self.nd.get(*['hello2'], **d)
        self.assertEqual(value, 2)

        source = {'hello': 'to_override'}
        overrides = {'hello': 'over'}
        d = self.nd.update2(overrides, **source)
        self.assertEqual(d, {'hello': 'over'})

        source = {'hello': {'value': 'to_override', 'no_change': 1}}
        overrides = {'hello': {'value': 'over'}}
        d = self.nd.update2(overrides, **source)
        self.assertEqual(d, {'hello': {'value': 'over', 'no_change': 1}})
        value = self.nd.get(*['hello', 'no_change'], **source)
        self.assertEqual(value, 1)

        source = {'hello': {'value': 'to_override', 'no_change': 1}}
        overrides = {'hello': {'value': {}}}
        dnew = self.nd.update2(overrides, **source)
        self.assertEqual(dnew, {'hello': {'value': {}, 'no_change': 1}})

        source = {'hello': {'value': {}, 'no_change': 1}}
        overrides = {'hello': {'value': 2}}
        dnew = self.nd.update2(overrides, **source)
        self.assertEqual(dnew, {'hello': {'value': 2, 'no_change': 1}})
