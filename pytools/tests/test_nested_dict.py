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
        v = self.nd.get(keys=['a', 'b', 'c'], dold=self.d)
        self.assertEqual(v, 'C')

        # depth 0
        dc = copy.deepcopy(self.d)
        items = ['x', 'y', 'z']
        dnew = self.nd.set(value='E', keys=items, dold=dc)
        v = self.nd.get(keys=['x', 'y', 'z'], dold=dnew)
        self.assertEqual(v, 'E')

        # depth 1
        dc = copy.deepcopy(self.d)
        items = ['a', 'y', 'z']
        dnew = self.nd.set(value='E', keys=items, dold=dc)
        v = self.nd.get(keys=['a', 'y', 'z'], dold=dnew)
        self.assertEqual(v, 'E')

        # depth 2
        dc = copy.deepcopy(self.d)
        items = ['a', 'b', 'e']
        dnew = self.nd.set(value='E', keys=items, dold=dc)
        v = self.nd.get(keys=['a', 'b', 'e'], dold=dnew)
        self.assertEqual(v, 'E')

        # depth 3
        dc = copy.deepcopy(self.d)
        items = ['a', 'b', 'c']
        dnew = self.nd.set(value='E', keys=items, dold=dc)
        v = self.nd.get(keys=['a', 'b', 'c'], dold=dnew)
        self.assertEqual(v, 'E')

    def test_set(self):
        # update the lastdict with new value of the same key
        dcopy = copy.deepcopy(self.dfood)
        dnew = self.nd.set(value='topless', keys=[u'0002', u'topping', u'5001', u'type'],  dold=dcopy)
        value = self.nd.get(keys=[u'0002', u'topping', u'5001'], dold=dnew)
        self.assertEqual(value, {'id': '5001', 'type': 'topless'})

        # update the lastdict with new key: value, but not new dict
        dcopy = copy.deepcopy(self.dfood)
        dnew = self.nd.set(value='5.01', keys=['0002', 'topping', '5001', 'price'], dold=dcopy)
        value = self.nd.get(keys=['0002', 'topping', '5001'], dold=dnew)
        self.assertEqual(value, {'id': '5001', 'type': u'None', 'price': '5.01'})

        # int key
        dcopy = copy.deepcopy(self.dfood)
        dnew = self.nd.set(value='topless', keys=[35, 'topping', '5001', 'type'],  dold=dcopy)
        pprint(dnew)
        argv = [35, 'topping', '5001']
        value = self.nd.get(keys=argv, dold=dnew)
        self.assertEqual(value, {'type': 'topless'})

    def test_create(self):
        keys = ['a', 'b', 'c']
        value = {u'd': 1}
        d = self.nd.create(value=value, keys=keys)
        dnew = {'a': {'b': {'c': {u'd': 1}}}}
        self.assertEqual(d, dnew)

    def test_update(self):
        d_original = {'hello1': 1}
        dup = {'hello2': 2}
        d = self.nd.update(dnew=dup, dold=d_original)
        self.assertEqual(d, {'hello1': 1, 'hello2': 2})

        # d_original did not change
        self.assertEqual(set(d.keys()), set(['hello1', 'hello2']))
        # dold in parameters will be updated(!)
        # self.assertEqual(d_original.keys(), ['hello1'])

        value = self.nd.get(keys=['hello2'], dold=d)
        self.assertEqual(value, 2)

        d_original = {'hello': 'to_override'}
        dup = {'hello': 'over'}
        d = self.nd.update(dnew=dup, dold=d_original)
        self.assertEqual(d, {'hello': 'over'})

        d_original = {'hello': {'value': 'to_override', 'no_change': 1}}
        dup = {'hello': {'value': 'over'}}
        d = self.nd.update(dnew=dup, dold=d_original)
        self.assertEqual(d, {'hello': {'value': 'over', 'no_change': 1}})
        value = self.nd.get(keys=['hello', 'no_change'], dold=d_original)
        self.assertEqual(value, 1)

        d_original = {'hello': {'value': 'to_override', 'no_change': 1}}
        dup = {'hello': {'value': {}}}
        dnew = self.nd.update(dnew=dup, dold=d_original)
        self.assertEqual(dnew, {'hello': {'value': {}, 'no_change': 1}})

        d_original = {'hello': {'value': {}, 'no_change': 1}}
        dup = {'hello': {'value': 2}}
        dnew = self.nd.update(dnew=dup, dold=d_original)
        self.assertEqual(dnew, {'hello': {'value': 2, 'no_change': 1}})

    def test_merge_shallow(self):
        d = {}
        dnew = {}
        du = self.nd.merge_shallow(dnew=dnew, dold=d)
        self.assertEqual(du, d)

        d_original = {'hello1': 1}
        dup = {'hello2': 2}
        du = self.nd.merge_shallow(dnew=dup, dold=d_original)
        self.assertEqual(du, {'hello1': 1, 'hello2': 2})

        # this is not shallow
        d_original = {'hello': {'value': 'to_override', 'no_change': 1}}
        dup = {'hello': {'value': 'over'}}

        d = self.nd.merge_shallow(dnew=dup, dold=d_original)
        self.assertEqual(d, {'hello': {'value': 'over'}})

    def test_update2(self):
        d_original = {'hello1': 1}
        dup = {'hello2': 2}
        d = self.nd.update2(dnew=dup, dold=d_original)
        self.assertEqual(d, {'hello1': 1, 'hello2': 2})

        # d_original did not change
        self.assertEqual(set(d.keys()), set(['hello1', 'hello2']))
        # self.assertEqual(d_original.keys(), ['hello1'])

        value = self.nd.get(keys=['hello2'], dold=d)
        self.assertEqual(value, 2)

        d_original = {'hello': 'to_override'}
        dup = {'hello': 'over'}
        d = self.nd.update2(dnew=dup, dold=d_original)
        self.assertEqual(d, {'hello': 'over'})

        d_original = {'hello': {'value': 'to_override', 'no_change': 1}}
        dup = {'hello': {'value': 'over'}}
        d = self.nd.update2(dnew=dup, dold=d_original)
        self.assertEqual(d, {'hello': {'value': 'over', 'no_change': 1}})

        value = self.nd.get(keys=['hello', 'no_change'], dold=d_original)
        self.assertEqual(value, 1)

        d_original = {'hello': {'value': 'to_override', 'no_change': 1}}
        dup = {'hello': {'value': {}}}
        dnew = self.nd.update2(dnew=dup, dold=d_original)
        self.assertEqual(dnew, {'hello': {'value': {}, 'no_change': 1}})

        d_original = {'hello': {'value': {}, 'no_change': 1}}
        dup = {'hello': {'value': 2}}
        dnew = self.nd.update2(dnew=dup, dold=d_original)
        self.assertEqual(dnew, {'hello': {'value': 2, 'no_change': 1}})

    def test_update_a(self):
        d_original = {'hello1': 1}
        dup = {'hello2': 2}
        d = self.nd.update(dnew=dup, dold=d_original)
        self.assertEqual(d, {'hello1': 1, 'hello2': 2})

        # d_original did not change
        self.assertEqual(set(d.keys()), set(['hello1', 'hello2']))
        # self.assertEqual(d_original.keys(), ['hello1'])

        value = self.nd.get(keys=['hello2'], dold=d)
        self.assertEqual(value, 2)

        d_original = {'hello': 'to_override'}
        dup = {'hello': 'over'}
        d = self.nd.update(dnew=dup, dold=d_original)
        self.assertEqual(d, {'hello': 'over'})

        d_original = {'hello': {'value': 'to_override', 'no_change': 1}}
        dup = {'hello': {'value': 'over'}}
        d = self.nd.update(dnew=dup, dold=d_original)
        self.assertEqual(d, {'hello': {'value': 'over', 'no_change': 1}})

        value = self.nd.get(keys=['hello', 'no_change'], dold=d_original)
        self.assertEqual(value, 1)

        d_original = {'hello': {'value': 'to_override', 'no_change': 1}}
        dup = {'hello': {'value': {}}}
        dnew = self.nd.update(dnew=dup, dold=d_original)
        self.assertEqual(dnew, {'hello': {'value': {}, 'no_change': 1}})

        d_original = {'hello': {'value': {}, 'no_change': 1}}
        dup = {'hello': {'value': 2}}
        dnew = self.nd.update(dnew=dup, dold=d_original)
        self.assertEqual(dnew, {'hello': {'value': 2, 'no_change': 1}})
