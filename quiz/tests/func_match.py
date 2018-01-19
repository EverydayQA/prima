import argparse
import sys
import os


class FuncList(object):

    def __init__(self, pfile):
        self.pfile = pfile

    def cls_list(self):
        """
        :rtype: list(clsName)
        """
        return []

    def get_func_d(self):
        """
        list(func) - possible class Name
        """
        d = {}
        alist = []
        d['clsname'] = alist
        return d

    def get_valid_func_name(self, line):
        return 'valid_name'


class FuncMatch(object):

    def __init__(self, argv):
        self.argv = argv
        args, args_extra = self.init_args()
        self.args = args
        self.args_extra = args_extra

    def init_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--test', type=str, default=None, help='test python file')
        args, args_extra = parser.parse_known_args(self.argv)
        return args, args_extra

    @property
    def test_file(self):
        return self.get_test_file()

    def get_file_root(self, afile):
        bname = os.path.basename(afile)
        bname = bname.replace('test_', '')
        return bname

    def find_original_python(self, fdir):
        root_dir = os.path.abspath(fdir)
        lp = []
        bname_test = self.get_file_root(self.test_file)

        for dirName, subdirList, fileList in os.walk(root_dir):
            for fname in fileList:
                if fname.endswith('.py'):
                    bname_o = self.get_file_root(fname)
                    if bname_o == bname_test:
                        fpath = os.path.join(root_dir, dirName, fname)
                        lp.append(fpath)
        return lp

    def get_cls_list(self):
        o_cls_list = []
        t_cls_list = []
        o_func_d = {}
        t_func_d = {}

    def append_d_to_test_file(self, d):
        pass

    def get_test_file(self):
        if self.args.test:
            return self.args.test
        for item in self.args_extra:
            if os.path.isfile(item):
                if item.endswith('.py'):
                    return item
        return None

    def match(self):
        if not self.test_file:
            print 'not test python file'
            return
        print 'using {}'.format(self.test_file)
        lp = self.find_original_python('../')
        print 'found original python'
        print lp


def main(argv):
    fm = FuncMatch(argv)
    fm.match()

if __name__ == '__main__':
    main(sys.argv[1:])
