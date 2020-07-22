import unittest
import json
import os
import copy
from nested.nested_dict import NestedDict
from pprint import pprint


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
        v = self.nd.get(keys=['a', 'b', 'c'], dnow=self.d)
        self.assertEqual(v, 'C')

        # depth 0
        dc = copy.deepcopy(self.d)
        items = ['x', 'y', 'z']
        dchg = self.nd.set(value='E', keys=items, dnow=dc)
        v = self.nd.get(keys=['x', 'y', 'z'], dnow=dchg)
        self.assertEqual(v, 'E')

        # depth 1
        dc = copy.deepcopy(self.d)
        items = ['a', 'y', 'z']
        dchg = self.nd.set(value='E', keys=items, dnow=dc)
        v = self.nd.get(keys=['a', 'y', 'z'], dnow=dchg)
        self.assertEqual(v, 'E')

        # depth 2
        dc = copy.deepcopy(self.d)
        items = ['a', 'b', 'e']
        dchg = self.nd.set(value='E', keys=items, dnow=dc)
        v = self.nd.get(keys=['a', 'b', 'e'], dnow=dchg)
        self.assertEqual(v, 'E')

        # depth 3
        dc = copy.deepcopy(self.d)
        items = ['a', 'b', 'c']
        dchg = self.nd.set(value='E', keys=items, dnow=dc)
        v = self.nd.get(keys=['a', 'b', 'c'], dnow=dchg)
        self.assertEqual(v, 'E')

    def test_set(self):
        # update the lastdict with new value of the same key
        dcopy = copy.deepcopy(self.dfood)
        dchg = self.nd.set(value='topless', keys=[u'0002', u'topping', u'5001', u'type'],  dnow=dcopy)
        value = self.nd.get(keys=[u'0002', u'topping', u'5001'], dnow=dchg)
        self.assertEqual(value, {'id': '5001', 'type': 'topless'})

        # update the lastdict with new key: value, but not new dict
        dcopy = copy.deepcopy(self.dfood)
        dchg = self.nd.set(value='5.01', keys=['0002', 'topping', '5001', 'price'], dnow=dcopy)
        value = self.nd.get(keys=['0002', 'topping', '5001'], dnow=dchg)
        self.assertEqual(value, {'id': '5001', 'type': u'None', 'price': '5.01'})

        # int key
        dcopy = copy.deepcopy(self.dfood)
        dchg = self.nd.set(value='topless', keys=[35, 'topping', '5001', 'type'],  dnow=dcopy)
        pprint(dchg)
        argv = [35, 'topping', '5001']
        value = self.nd.get(keys=argv, dnow=dchg)
        self.assertEqual(value, {'type': 'topless'})

        # special condition  value to be dict
        dcopy = copy.deepcopy(self.dfood)
        dnew = {'id': 555, 'type': 'berry', 'price': 0.99}
        dchg = self.nd.set(value=dnew, keys=['0002', 'topping', '5001'], dnow=dcopy)

        value = self.nd.get(keys=['0002', 'topping', '5001'], dnow=dchg)
        pprint(value)
        self.assertEqual(value, dnew)

        # without id
        dcopy = copy.deepcopy(self.dfood)
        dnew = {'Type': 'berry', 'price': 0.99}
        dchg = self.nd.set(value=dnew, keys=['0002', 'topping', '5001'], dnow=dcopy)
        value = self.nd.get(keys=['0002', 'topping', '5001'], dnow=dchg)
        self.assertEqual(value, {u'id': u'5001', 'Type': 'berry', 'price': 0.99, u'type': u'None'})

    def test_create(self):
        keys = ['a', 'b', 'c']
        value = {u'd': 1}
        d = self.nd.create(value=value, keys=keys)
        dchg = {'a': {'b': {'c': {u'd': 1}}}}
        self.assertEqual(d, dchg)

    def test_update(self):
        d_original = {'hello1': 1}
        dup = {'hello2': 2}
        d = self.nd.update(dchg=dup, dnow=d_original)
        self.assertEqual(d, {'hello1': 1, 'hello2': 2})

        # d_original did not change
        self.assertEqual(set(d.keys()), set(['hello1', 'hello2']))
        # dnow in parameters will be updated(!)
        # self.assertEqual(d_original.keys(), ['hello1'])

        value = self.nd.get(keys=['hello2'], dnow=d)
        self.assertEqual(value, 2)

        d_original = {'hello': 'to_override'}
        dup = {'hello': 'over'}
        d = self.nd.update(dchg=dup, dnow=d_original)
        self.assertEqual(d, {'hello': 'over'})

        d_original = {'hello': {'value': 'to_override', 'no_change': 1}}
        dup = {'hello': {'value': 'over'}}
        d = self.nd.update(dchg=dup, dnow=d_original)
        self.assertEqual(d, {'hello': {'value': 'over', 'no_change': 1}})
        value = self.nd.get(keys=['hello', 'no_change'], dnow=d_original)
        self.assertEqual(value, 1)

        d_original = {'hello': {'value': 'to_override', 'no_change': 1}}
        dup = {'hello': {'value': {}}}
        dchg = self.nd.update(dchg=dup, dnow=d_original)
        self.assertEqual(dchg, {'hello': {'value': {}, 'no_change': 1}})

        d_original = {'hello': {'value': {}, 'no_change': 1}}
        dup = {'hello': {'value': 2}}
        dchg = self.nd.update(dchg=dup, dnow=d_original)
        self.assertEqual(dchg, {'hello': {'value': 2, 'no_change': 1}})

    def test_merge_shallow(self):
        d = {}
        dchg = {}
        du = self.nd.merge_shallow(dchg=dchg, dnow=d)
        self.assertEqual(du, d)

        d_original = {'hello1': 1}
        dup = {'hello2': 2}
        du = self.nd.merge_shallow(dchg=dup, dnow=d_original)
        self.assertEqual(du, {'hello1': 1, 'hello2': 2})

        # this is not shallow
        d_original = {'hello': {'value': 'to_override', 'no_change': 1}}
        dup = {'hello': {'value': 'over'}}

        d = self.nd.merge_shallow(dchg=dup, dnow=d_original)
        self.assertEqual(d, {'hello': {'value': 'over'}})

    def test_update2(self):
        d_original = {'hello1': 1}
        dup = {'hello2': 2}
        d = self.nd.update2(dchg=dup, dnow=d_original)
        self.assertEqual(d, {'hello1': 1, 'hello2': 2})

        # d_original did not change
        self.assertEqual(set(d.keys()), set(['hello1', 'hello2']))
        # self.assertEqual(d_original.keys(), ['hello1'])

        value = self.nd.get(keys=['hello2'], dnow=d)
        self.assertEqual(value, 2)

        d_original = {'hello': 'to_override'}
        dup = {'hello': 'over'}
        d = self.nd.update2(dchg=dup, dnow=d_original)
        self.assertEqual(d, {'hello': 'over'})

        d_original = {'hello': {'value': 'to_override', 'no_change': 1}}
        dup = {'hello': {'value': 'over'}}
        d = self.nd.update2(dchg=dup, dnow=d_original)
        self.assertEqual(d, {'hello': {'value': 'over', 'no_change': 1}})

        value = self.nd.get(keys=['hello', 'no_change'], dnow=d_original)
        self.assertEqual(value, 1)

        d_original = {'hello': {'value': 'to_override', 'no_change': 1}}
        dup = {'hello': {'value': {}}}
        dchg = self.nd.update2(dchg=dup, dnow=d_original)
        self.assertEqual(dchg, {'hello': {'value': {}, 'no_change': 1}})

        d_original = {'hello': {'value': {}, 'no_change': 1}}
        dup = {'hello': {'value': 2}}
        dchg = self.nd.update2(dchg=dup, dnow=d_original)
        self.assertEqual(dchg, {'hello': {'value': 2, 'no_change': 1}})
