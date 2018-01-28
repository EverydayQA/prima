from pprint import pprint
import collections
import re
import os
from termcolor import cprint


class ParseDump(object):
    """
    Explore how to Read File with Indentation to a dictionary
    """

    def __init__(self, afile):
        self.afile = afile

    def lines_file(self):
        with open(self.afile, mode='r') as f:
            lines = f.readlines()
            return lines
        return []

    def normalize_key(self, key):
        if not key:
            return key
        key = key.strip()
        key = key.lstrip('/')
        key = key.strip()
        key = key.strip(':')
        key = key.strip()
        key = key.lstrip('_')
        key = key.replace(' ', '_')
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

    def get_subkeys(self, line):
        d = {}
        items = line.split('=')
        if not items:
            return d
        value = items.pop()
        value = self.normalize_value(value)
        d['value'] = value
        if not items:
            return d
        subkey = items.pop(0)
        subkey = self.normalize_key(subkey)
        keys = subkey.split(':')
        subkeys = []
        for key in keys:
            key = self.normalize_key(key)
            subkeys.append(key)
        d['subkeys'] = subkeys
        return d

    def d_file(self):
        """
        To be modified to use recursive
        """
        d = {}
        lines = self.lines_file()
        lines = self.lines_normalize(lines)
        key = None
        for line in lines:
            if len(line) < 3:
                continue
            line = line.rstrip('\n')
            if line.startswith('\t') or line.startswith(' '):
                if not key:
                    cprint(line, 'red')
                    continue
                d_nexts = self.get_subkeys(line)
                subkeys = d_nexts.get('subkeys', [])
                value = d_nexts.get('value', None)
                if subkeys:
                    dd = self.get_dict_with_keys_3(subkeys, value)
                    # previous entries in d for the key
                    d_prev = d.get(key, {})

                    # to include df in the dict
                    d_prev.update(dd)
                    d[key] = d_prev
            else:
                # key
                key = self.normalize_key(line)
        return d

    def update(self, d, u):
        """
        Not working as expected, as this code is copied from ...
        """
        for k, v in u.iteritems():
            if isinstance(v, collections.Mapping):
                d[k] = self.update(d.get(k, {}), v)
            else:
                d[k] = v
        return d

    def get_dict_with_keys_3(self, keys, value):
        """
        For all subkeys, get dict with 1 entry for all subkeys
        """
        d = {}
        d_prev = {}
        for key in reversed(keys):
            dn = {}
            if key == keys[-1]:
                dn[key] = value
            else:
                dn = d.get(key, {})
                dn[key] = d_prev

            if key == keys[0]:
                return dn
            d_prev = dn
        return d

    def get_dict_with_keys_2(self, keys, value):
        """
        For all subkeys, get dict with 1 entry for all subkeys
        """
        d_prev = {}
        for key in reversed(keys):
            dn = {}
            if key == keys[-1]:
                dn[key] = value
            else:
                dn[key] = d_prev

            if key == keys[0]:
                return dn
            d_prev = dn
        return {}

    def get_dict_with_keys(self, keys, value):
        """
        For all subkeys, get dict with 1 entry for all subkeys
        """
        print 'keys<{}> value<{}>'.format(keys, value)
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
            print '{} {}'.format(i, c)
        return 0

    def parse(self):
        d = self.d_file()
        return d


def main():
    path = os.path.dirname(__file__)
    afile = os.path.join(path, 'dump.txt')
    pd = ParseDump(afile)
    d = pd.parse()
    pprint(d)


if __name__ == '__main__':
    main()
