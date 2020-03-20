
import re
from termcolor import cprint
import json
from src.normalize_string import NormalizeString
from src.parse_line import DParseLine
from src.nested_dict import NestedDict


class DPaseFile(object):
    """
    Explore how to Read File with Indentation to a dictionary
    """

    def __init__(self, afile):
        self.nm = NormalizeString()
        self.nd = NestedDict()
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
        stored in nested dict
        """
        d = {}
        lines = self.lines_file(afile)
        key = None
        count = 0
        for line in lines:
            if len(line) < 3:
                continue
            count = count + 1
            if count > 5:
                break
            line = line.rstrip('\n')
            dpl = DParseLine(line)
            print('line: <{}>'.format(line))
            dl = dpl.d_keys_value(line)
            print(dl)
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

    def d_deep_get(self, d, keys, default=None):
        # return self.nd.d_deep_get(d, keys)
        dtmp = d
        for key in keys:
            if isinstance(dtmp, dict):
                dtmp = dtmp.get(key, default)
            else:
                return dtmp
        return dtmp

    def deepGet(self, d, *keys):
        return self.nd.deep_get(d, *keys)

    def deep_set(self, d, value, *keys):
        return self.nd.deep_set(d, value, *keys)

    def d_update(self, d, u):
        """
        u - dict with subkeys to be updated into d
        """
        return self.nd.deep_update(d, u)
