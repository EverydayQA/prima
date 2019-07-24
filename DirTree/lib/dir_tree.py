import os
from pprint import pprint


class DirTree(object):

    def __init__(self, path):
        self.path = path
        self.dtree = self.get_directory_structure(self.path)

    def get_directory_structure(self, rootdir):
        """
        Creates a nested dictionary that represents the folder structure of rootdir
        using os.walk -- slow in python2
        """
        d = {}
        print(rootdir)
        rootdir = rootdir.rstrip(os.sep)
        start = rootdir.rfind(os.sep) + 1
        for path, dirs, files in os.walk(rootdir):
            folders = path[start:].split(os.sep)
            subdir = dict.fromkeys(files)
            parent = reduce(dict.get, folders[:-1], d)
            parent[folders[-1]] = subdir
        return d


class DirTreeScandir(object):
    """
    tree structure using scandir
    """

    def __init__(self, path):
        self.path = path
        # self.dtree = self.get_directory_structure(self.path)
        self.dtree = self.d_walk(path)

    def get_directory_structure(self, rootdir):
        """
        avoid using os.walk -- too slow in python2
        """
        # from os import scandir
        import scandir

        for entry in scandir.scandir(rootdir):
            print('path {}'.format(entry.path))
            print('name {}'.format(entry.name))
            print('is_dir {}'.format(entry.is_dir()))
            print('is_file {}'.format(entry.is_file()))
            print('is_symlink {}'.format(entry.is_symlink()))

            print('inode {}'.format(entry.inode()))
            if not entry.name.startswith('.') and entry.is_dir():
                # yield entry.name
                pass

    def d_walk(self, rootdir):
        import scandir
        d = {}
        df = {}
        dp = {}
        for path, subdirs, files in scandir.walk(rootdir):
            if files:
                df[path] = files
            if subdirs:
                dp[path] = subdirs
        d['files'] = df
        # subdirs is not really useful? redundant? df should be enough
        # d['subdirs'] = dp
        return df


def main():
    path = os.getcwd()
    dt = DirTreeScandir(path)
    pprint(dt.dtree)


if __name__ == '__main__':
    main()
