from pprint import pprint
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

    def d_file(self):
        d = {}
        lines = self.lines_file()
        lines = self.lines_normalize(lines)
        items = []
        key = None
        for line in lines:
            if len(line) < 3:
                continue
            line = line.rstrip('\n')
            if line.startswith('\t') or line.startswith(' '):
                # subkey
                items = line.split('=')
                if key:
                    if len(items) == 2:
                        value = items[1]
                        value = value.strip()
                        key2 = items[0]
                        key2 = key2.strip()
                        eles = key2.split(':')
                        eles = filter(None, eles)
                        if len(eles) == 2:
                            key2 = eles[0]
                            key3 = eles[1]
                            d2 = d.get(key, {})
                            d3 = d2.get(key2, {})
                            d3[key3] = value
                            d2[key2] = d3
                            d[key] = d2
                        else:
                            ds = d.get(key, {})
                            ds[key2] = value
                            d[key] = ds
            else:
                # key
                key = line
        return d

    def count_leading_space(self, a):
        for i, c in enumerate(a):
            print '{} {}'.format(i, c)
        return 0

    def parse(self):
        d = self.d_file()
        pprint(d)


def main():
    path = os.path.dirname(__file__)
    afile = os.path.join(path, 'dump.txt')
    pd = ParseDump(afile)
    d = pd.parse()
    pprint(d)


if __name__ == '__main__':
    main()
