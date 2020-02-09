from pprint import pprint
import os
from src.parse_file import DPaseFile


class CliParseFile(object):

    def __init__(self):
        self.fdir = os.path.dirname(__file__)

    def file2d(self, afile):
        pf = DPaseFile(afile)
        return pf.d_file(afile)

    def get_afile(self):
        afile = os.path.join(self.fdir, '../data/dump.txt')
        return afile


def main():
    cli = CliParseFile()
    afile = cli.get_afile()
    print(afile)
    d = cli.file2d(afile)
    pprint(d)


if __name__ == "__main__":
    main()
