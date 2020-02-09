from .normalize_string import NormalizeString
import collections


class DParseLine(object):

    def __init__(self, line):
        """
        directory return d instead of holding a self.line
        """
        self.nm = NormalizeString()
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
