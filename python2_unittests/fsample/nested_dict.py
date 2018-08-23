import collections
import unittest
from pprint import pprint
import os
import copy


class NestedDict(object):
    """
    Before a nested dict in installed, this will be tested and used
    """

    def deep_update(self, source, overrides):
        """Update a nested dictionary or similar mapping.

        Modify ``source`` in place.
        """
        for key, value in overrides.iteritems():
            if isinstance(value, collections.Mapping) and value:
                returned = self.deep_update(source.get(key, {}), value)
                source[key] = returned
            else:
                source[key] = overrides[key]
        pprint(source)
        return source

    def d_deep_get(self, d_original, keys, default=None):
        items = list(keys)
        return self.deep_get_recursive(d_original, items)

    def deep_get_recursive(self, d, keys):
        if not d:
            return None
        if not keys:
            return None
        key = keys.pop(0)
        dv = d.get(key, None)
        if isinstance(dv, dict):
            return self.deep_get_recursive(dv, keys)
        else:
            return dv

    def deep_get_reduce(self, _dict, keys, default=None):

        def _reducer(d, key):
            if isinstance(d, dict):
                return d.get(key, default)
            return default

        return reduce(_reducer, keys, _dict)

    def deep_get(self, sourceDict, keys):
        # deepGet(mydict, *['level_one', 'level_two', 'test'])

        return reduce(lambda d, k: d.get(k) if d else None, keys, sourceDict)

    def deep_set(self, sourceDict, value, keys):
        # pop() the last item of the list, use your deepGet on it and set the popped off key on the resulting dict
        items = list(keys)
        last_key = items.pop()
        d = self.deep_get(sourceDict, items)
        d[last_key] = value
        return sourceDict


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
        d = self.nd.deep_get_reduce(self.d, ['a', 'b', 'c'], default='NA')
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
