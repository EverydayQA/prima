
import re
from termcolor import cprint
import json
from pprint import pprint
from src.normalize_string import NormalizeString
from src.parse_line import DParseLine
from src.nested_dict import NestedDict


class DPaseFile(object):
    """
    Explore how to Read File with Indentation to a dictionary
    """

    def __init__(self, afile):
        self.nm = NormalizeString()
        self.nested = NestedDict()
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
        lastkey = None
        for line in lines:
            line = line.rstrip('\n')
            line = line.lstrip('\n')
            line = line.strip()
            items = line.split(' ')

            # print('line: <{}> <{}>'.format(line, items))

            if '=' not in items:
                continue

            # lastkey not changed unless :
            if ':' in line:
                eles = items[0].split(':')
                lastkey = eles[0]
            dpl = DParseLine(line)
            d_nexts = dpl.d_keys_value(line, key=lastkey)
            pprint(d_nexts)

            keys = d_nexts.get('keys', [])
            value = d_nexts.get('value', None)
            cprint('lastkey {} keys {} value {}>'.format(lastkey, keys, value), 'green')

            dnest = self.nested.create_nested(keys, value)
            pprint(dnest)
            d = self.nested.update_nested(d, dnest)
        return d

    def d_deep_get(self, d, keys, default=None):
        dtmp = d
        for key in keys:
            if isinstance(dtmp, dict):
                dtmp = dtmp.get(key, default)
            else:
                return dtmp
        return dtmp

    def deepGet(self, d, *keys):
        return self.nested.deep_get(d, *keys)

    def deep_set(self, d, value, *keys):
        return self.nested.deep_set(d, value, *keys)

    def d_update(self, d, u):
        """
        u - dict with subkeys to be updated into d
        """
        return self.nested.deep_update(d, u)
