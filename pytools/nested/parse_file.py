
import re
from termcolor import cprint
import json
from pprint import pprint
from nested.normalize_string import NormalizeString
from nested.parse_line import DParseLine
from nested.nested_dict import NestedDict


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

            dnest = self.nested.create(value, *keys)
            pprint(dnest)
            d = self.nested.update(dnest, **d)
        return d
