
import collections
import re
from termcolor import cprint
import json
from src.normalize_string import NormalizeString
from src.parse_line import DParseLine


class DPaseFile(object):
    """
    Explore how to Read File with Indentation to a dictionary
    """

    def __init__(self, afile):
        self.nm = NormalizeString()
        self.df = self.d_file(afile)

    def fout(self):
        """
        output file to tmpdir
        """
        return '/tmp/header.json'

    def write_2tmpdir(self, d):
        with open(self.fout(), 'w') as f:
            json.dump(d, f, ensure_ascii=False, indent=4)

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

    def python2_d_deep_get(self, dictionary, keys, default=None):
        # import function_tools
        # return function_tools.reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)
        pass

    def d_deep_get(self, d, keys, default=None):
        dtmp = d
        for key in keys:
            if isinstance(dtmp, dict):
                dtmp = dtmp.get(key, default)
            else:
                return dtmp
        return dtmp

    def deepGet(self, d, *keys):
        dtmp = d
        for key in keys:
            if isinstance(dtmp, dict):
                dtmp = dtmp.get(key, None)
            else:
                return dtmp
        return dtmp

    def deep_set(self, d, value, *keys):
        # pop() the last item of the list, use your deepGet on it and set the popped off key on the resulting dict
        last_key = keys.pop()
        dnew = self.deepGet(d, *keys)
        dnew[last_key] = value
        return dnew

    def d_update(self, d, u):
        """
        u - dict with subkeys to be updated into d
        """
        for k in u.keys():
            v = u.det(k, None)
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
        for key in overrides.keys():
            value = overrides.get(key, None)
            if isinstance(value, collections.Mapping) and value:
                returned = self.deep_update(source.get(key, {}), value)
                source[key] = returned
            else:
                source[key] = overrides[key]
        return source
