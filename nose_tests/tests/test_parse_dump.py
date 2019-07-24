from pprint import pprint
import collections
import re
import os
from termcolor import cprint
import json
import unittest


class DPaseFile(object):
    """
    Explore how to Read File with Indentation to a dictionary
    """

    def __init__(self, afile):
        self.nm = NormalizeMincinfo()
        self.df = self.d_file(afile)
        with open('/tmp/data.json', 'w') as f:
            json.dump(self.df, f, ensure_ascii=False, indent=4)

    def txt_from_file(self, afile):
        with open(afile, mode='r') as f:
            return f.read()
        return ''

    def lines_file(self, afile):
        txt = self.txt_from_file(afile)
        lines = re.split(';\n', txt)
        return lines

    def d_file(self, afile):
        """
        To be modified to use recursive
        """
        d = {}
        lines = self.lines_file(afile)
        key = None
        for line in lines:
            if len(line) < 3:
                continue
            line = line.rstrip('\n')
            dpl = DParseLine(line)
            if line.startswith('\t') or line.startswith(' '):
                if not key:
                    cprint(line, 'red')
                    continue

                d_nexts = dpl.d_keys_value(line)
                subkeys = d_nexts.get('subkeys', [])
                value = d_nexts.get('value', None)
                if subkeys:
                    dd = dpl.d_deep_set_keys_value(subkeys, value)
                    # previous entries in d for the key
                    d_key = d.get(key, {})

                    # this is a dict internal function to update
                    # to include dd in the dict
                    d_key.update(dd)
                    d[key] = d_key
            else:
                # key
                key = dpl.nm.normalize_key(line)
        return d

    def d_deep_get(self, dictionary, keys, default=None):
        return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)

    def deepGet(self, sourceDict, *keys):
        # deepGet(mydict, *['level_one', 'level_two', 'test'])
        return reduce(lambda d, k: d.get(k) if d else None, keys, sourceDict)

    def deep_set(self, sourceDict, value, *keys):
        # pop() the last item of the list, use your deepGet on it and set the popped off key on the resulting dict
        last_key = keys.pop()
        d = self.deepGet(sourceDict, *keys)
        d[last_key] = value
        return d

    def d_update(self, d, u):
        """
        u - dict with subkeys to be updated into d
        """
        for k, v in u.iteritems():
            if isinstance(v, collections.Mapping):
                d[k] = self.update(d.get(k, {}), v)
            else:
                d[k] = v
        return d

    def lines_normalize(self, lines):
        items = []
        hold = []
        for line in lines:
            line = line.rstrip()
            if line == '':
                continue
            if line.endswith(','):
                cprint(line, 'red')
                if hold:
                    line = line.strip()
                hold.append(line)
                continue
            else:
                if hold:
                    line = line.strip()
                    hold.append(line)
                    line = ' '.join(hold)
                hold = []
            items.append(line)
        return items

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
        return source


class TestDPaseFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        path = os.path.dirname(__file__)
        cls.afile = os.path.join(path, 'data/dump.txt')
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
        self.pd.deep_update(source, overrides)
        self.assertEqual(source, {'hello1': 1, 'hello2': 2})

        source = {'hello': 'to_override'}
        overrides = {'hello': 'over'}
        self.pd.deep_update(source, overrides)
        self.assertEqual(source, {'hello': 'over'})

        source = {'hello': {'value': 'to_override', 'no_change': 1}}
        overrides = {'hello': {'value': 'over'}}
        self.pd.deep_update(source, overrides)
        self.assertEqual(source, {'hello': {'value': 'over', 'no_change': 1}})

        source = {'hello': {'value': 'to_override', 'no_change': 1}}
        overrides = {'hello': {'value': {}}}
        self.pd.deep_update(source, overrides)
        self.assertEqual(source, {'hello': {'value': {}, 'no_change': 1}})

        source = {'hello': {'value': {}, 'no_change': 1}}
        overrides = {'hello': {'value': 2}}
        self.pd.deep_update(source, overrides)
        self.assertEqual(source, {'hello': {'value': 2, 'no_change': 1}})

    def test_dict_to_json(self):
        """
        """
        self.assertTrue(isinstance(self.d, dict))
        # json.dumps() converts a dictionary to str object,
        json_file = json.dumps(self.d)
        self.assertTrue(isinstance(json_file, basestring))
        # Output str
        print(type(json_file))

        # so you have to load your str into a dict to use it by using json.loads() method
        json_obj = json.loads(json_file)
        # equal to initial dict
        self.assertEqual(json_obj, self.d)
        pprint(json_obj)

        self.assertTrue(isinstance(json_obj, dict))
        self.assertFalse('listName' in json_obj)


class DParseLine(object):

    def __init__(self, line):
        """
        directory return d instead of holding a self.line
        """
        self.nm = NormalizeMincinfo()
        self.line = line

    def d_deep_set_keys_value(self, keys, value):
        """
        A generic func to set nested dict with a value with a set of keys
        """
        if not keys:
            return {}
        d_prev = {}
        for key in reversed(keys):
            dn = {}
            if key == keys[-1]:
                dn[key] = value
                d_prev = dn
                continue
            dn[key] = d_prev
            if key == keys[0]:
                return dn
            d_prev = dn
        return {}

    def get_dict_with_keys(self, keys, value):
        """
        For all subkeys, get dict with 1 entry for all subkeys
        """
        print('keys<{}> value<{}>'.format(keys, value))
        d = {}
        if len(keys) == 2:
            d2 = {}
            d2[keys[1]] = value
            d = {}
            d[keys[0]] = d2
            return d
        elif len(keys) == 1:
            d2 = {}
            d2[keys[0]] = value
            return d2

        return d

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
        return source

    def recursive_update_d(self, d, d_prev, key_prev, subkeys, value):
        """
        Disabled as it is too complicated
        For all subkeys, get dict with 1 entry for all subkeys
        This is not ideal with many parameters
        To be modified as different name, this sub will be kept for review
        """
        if not subkeys:
            return d_prev, key_prev

        subkey = subkeys.pop()
        d_now = d.get(subkey, {})

        if not key_prev:
            d_now[subkey] = value
        else:
            d_now[subkey] = d_prev
        return self.recursive_update_d(d, d_now, subkey, subkeys, value)

    def count_leading_space(self, a):
        for i, c in enumerate(a):
            print('{} {}'.format(i, c))
        return 0

    def d_keys_value(self, line):
        d = {}
        items = line.split('=')
        if not items:
            return d
        value = items.pop()
        value = self.nm.normalize_value(value)
        d['value'] = value
        if not items:
            return d
        subkey = items.pop(0)
        subkey = self.nm.normalize_key(subkey)
        if not subkey:
            return {}
        keys = subkey.split(':')
        subkeys = []
        for key in keys:
            key = self.nm.normalize_key(key)
            subkeys.append(key)
        d['subkeys'] = subkeys
        return d


class TestDparseLine(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.line1 = '		dicom_0x0028:el_0x0030 = "0.859375\\0.859375 " ;'
        cls.dpl = DParseLine(cls.line1)
        pass

    def test_deep_set(self):
        pass

    def test_d_keys_value(self):
        d = self.dpl.d_keys_value(self.line1)
        keys = d.get('subkeys', [])
        self.assertEqual(keys, ['dicom_0x0028', 'el_0x0030'])
        value = d.get('value', None)
        self.assertEqual(value, '0.859375\\0.859375')

    def test_d_deep_set_keys_value(self):
        """
        a test file with expected results
        """
        d = self.dpl.d_keys_value(self.line1)
        dd = self.dpl.d_deep_set_keys_value(d.get('subkeys', []), d.get('value', None))
        self.assertEqual(dd, {'dicom_0x0028': {'el_0x0030': '0.859375\\0.859375'}})


class NormalizeMincinfo(object):

    def __init__(self):
        """
        Intend to be generic class without taking any vars
        """
        pass

    def strip_chars(self):
        return ['/', ':', '_']

    def r_strip(self, line):
        if not line:
            return line
        size = len(line)
        for char in self.strip_chars():
            line = line.strip()
            line = line.strip(char)
            line = line.strip()
        if len(line) == size:
            return line
        return self.r_strip(line)

    def normalize_key(self, key):
        print(key)
        if not key:
            return key
        key = self.r_strip(key)
        if not key:
            return key
        key = key.replace(' ', '-')
        return key

    def normalize_value(self, value):
        if not value:
            return value
        # rermove <;>
        value = value.strip(';')

        # remove leading and trailing tab space
        value = value.strip()

        # remove <\\n>
        value = value.replace('\\n', '')

        # replace <\\> with <\>
        value = value.replace('\\\\', '\\')
        # find all instances of ""
        matches = re.findall(r'\"(.+?)\"', value)
        if not matches:
            return value

        items = []
        for match in matches:
            match = match.strip()
            # multiple spaces into one
            match = ' '.join(match.split())
            match = match.rstrip('_')
            if match:
                items.append(match)
        if not items:
            return ''
        if len(items) == 1:
            return items[0]
        return items


class TestNormalizeMincinfo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.nm = NormalizeMincinfo()

    def test_r_strip(self):
        key = ' 1234 ]-: '
        nkey = self.nm.r_strip(key)
        self.assertEqual(nkey, '1234 ]-')

    def test_normalize_key(self):
        key = ' 1234 ]-: '
        nkey = self.nm.normalize_key(key)
        self.assertEqual(nkey, '1234-]-')

    def test_normalize_value(self):
        v = '    sth stupid ;'
        nv = self.nm.normalize_value(v)
        self.assertEqual(nv, 'sth stupid')
