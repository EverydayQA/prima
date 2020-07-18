from pprint import pprint
import json
import os
from nested.nested_dict import NestedDict


class CliNested(object):

    def __init__(self):
        self.nested = NestedDict()

    def read_jsonfile(self, jfile):
        with open(jfile) as f:
            d = json.load(f)
            return d
        return {}

    def update(self, jfile):
        """
        practice
        to update into a deeper dict to test methods
        """
        print(jfile)
        if not os.path.isfile(jfile):
            return {}
        d = self.read_jsonfile(jfile)
        pprint(d)

        # set float
        keys = ['0003', 'topping', '5002', 'price']
        dnew = self.nested.set(keys, 1.99, **d)
        pprint(dnew)
        value = self.nested.get(dnew, keys)
        print(value)

        # dict
        dnew = self.nested.set(keys, {u'CAD': 1.99}, **d)
        pprint(dnew)
        value = self.nested.get(dnew, keys)
        print(value)

        # existing
        keys = ['0003', 'topping', '5002', 'type']
        dnew = self.nested.set(keys, 'topless', **d)
        pprint(dnew)
        value = self.nested.get(dnew, keys)
        print(value)

    def dump_to_json(self, dnew):
        newfile = '/tmp/food_nested_dict.json'
        with open(newfile, 'w') as fp:
            json.dump(dnew, fp, indent=4)


def main(argv=None):
    from args.nested_dict import ArgsNestedDict
    arg = ArgsNestedDict()
    args = arg.parse_args(argv)
    pprint(args)
    cli = CliNested()
    cli.update(args.file)


def howto(self):
    """
    PYTHONPATH=. python cli/cli_example.py -m a b c --a no --a yes --a nohold --a nrx3 -a b -m " --nohold"  " --nnn4" " --nocheck" " --job" " -j" --job 2 4 5 6
    ord_args() and chr_args are crazy but works
    " --nocheck" with a space does work and could lstrip() or no need
    PYTHONPATH=. python cli/cli_example.py --default="--nohold --nocheck"
    PYTHONPATH=. python cli/cli_example.py --default="--default  2  -m a b c"
    """
    pass


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
