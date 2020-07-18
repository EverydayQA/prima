import sys
import argparse


class TmpDirCli(object):

    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        self.ns = argparse.Namespace(**kwargs)

    def clean(self):
        pass

    def create(self):
        pass

    def dispatch(self):
        """
        args here or main()
        """
        print(self.kwargs)
        print(self.ns)


def main(argv=[]):
    print(argv)
    from args.tmpdir import ArgsTmpDir
    arg = ArgsTmpDir()
    args = arg.parse_argv(argv)
    print(args)
    tmpdir = TmpDirCli(**vars(args))
    tmpdir.dispatch()


if __name__ == '__main__':
    main(sys.argv[1:])
