from pprint import pprint
import os
import argparse
from src.parse_file import DPaseFile


class CliParseFile(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.fdir = os.path.dirname(__file__)
        self.dns = self.kwargs.get('dns', {})
        self.ns = argparse.Namespace(**self.dns)

    def file2d(self):
        afile = self.ns.file
        pf = DPaseFile(afile)
        return pf.d_file(afile)


def main(argv=None):
    from arg.parse_file import ArgParseFile
    par = ArgParseFile()
    args = par.get_args(argv)
    pprint(args)
    kwargs = {}
    kwargs['dns'] = vars(args)

    cli = CliParseFile(**kwargs)
    d = cli.file2d()
    pprint(d.keys())


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
