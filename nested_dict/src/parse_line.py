from .normalize_string import NormalizeString


class DParseLine(object):

    def __init__(self, line):
        """
        directory return d instead of holding a self.line
        """
        self.line = line
        self.nm = NormalizeString()

    def count_leading_space(self, a):
        for i, c in enumerate(a):
            print('{} {}'.format(i, c))
        return 0

    def d_keys_value(self, line, key=None):
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
        if ':' not in subkey:
            if key:
                keys = [key, subkey]
            else:
                keys = [subkey]
        else:
            keys = subkey.split(':')
        newkeys = []
        for key in keys:
            key = self.nm.normalize_key(key)
            newkeys.append(key)
        d['keys'] = newkeys
        return d
