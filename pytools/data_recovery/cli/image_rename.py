import os
import sys
import argparse


class DPath(object):
    """
    Go through subdir to find proper files wanted with certain conditions
    files restored by photorec without proper file names
    """

    def __init__(self, path):
        self.path = path
        self.dpath = self.d_walk(self.path)

    def d_walk(self, rootdir):
        df = {}
        for path, subdirs, files in os.walk(rootdir):
            if files:
                df[path] = list(set(files))
        return df


class CliImageRename(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.ns = argparse.Namespace(**self.kwargs)

    def rename(self):
        path = self.ns.path
        from img.rename_images import RenameImages
        ren = RenameImages(**self.kwargs)
        # ren.post_recovery_rename()
        ren.rename(path)


def main():
    from args.image_rename import ArgImageRename
    ren = ArgImageRename()
    args = ren.parse_args(sys.argv[1:])
    cli = CliImageRename(**vars(args))
    cli.rename()


if __name__ == '__main__':
    main()
