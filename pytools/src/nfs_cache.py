import os
import sys


class NfsCache(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def cycle_refresh(self, path):
        import time
        start_time = time.time()

        count = 70
        delta = 0
        while count > 0:
            self.refresh(path)
            delta = time.time() - start_time
            delta = float("{:.2f}".format(delta))
            if delta > 70:
                break
            print("{} --- {} secs {} ---".format(path, delta, count))

            time.sleep(1)
            count = count - 1

        print("{} --- {} secs {} ---".format(path, delta, count))

    def refresh(self, path):
        """
        nfs cache is  about 30 - 60 seconds depends
        """
        # first opendir closedir in perl
        # uppper dir -- important
        updir = os.path.dirname(path)
        os.chdir(updir)
        os.listdir()
        self.do_scandir(updir)
        self.do_walk(updir)
        os.chdir(path)

    def do_mincheader(self, minc):
        pass

    def do_scandir(self, path):
        """
        opendir/closedir
        """
        for item in os.scandir(path):
            if os.path.isdir(item):
                self.do_scandir(item)
            elif os.path.isfile(item):
                os.stat(item)

    def do_walk(self, path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                afile = os.path.join(root, name)
                os.stat(afile)
            for name in dirs:
                subdir = os.path.join(root, name)
                os.stat(subdir)


def main(argv=None):
    nfs = NfsCache()
    path = argv[0]
    print(argv)
    print(path)
    path = os.path.abspath(path)
    nfs.cycle_refresh(path)


if __name__ == '__main__':
    main(argv=sys.argv[1:])
