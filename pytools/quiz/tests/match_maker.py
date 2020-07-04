import argparse
import sys
import os
from pprint import pprint
import inspect
import importlib


class ModuleFunc(object):

    def __init__(self):
        pass

    def skip_builtin(self, obj):
        """ ModuleFunc a builtin function """
        print('+Built-in Function: %s' % obj.__name__)

    def skip_func(self, obj, method=False):
        """ ModuleFunc the function object passed as argument.
        If this is a method object, the second argument will
        be passed as True """

        if method:
            print('+Method: %s' % obj.__name__)
        else:
            print('+Function: %s' % obj.__name__)

    def module_funcs(self, obj):
        """
        functions of a modulue
        """
        print('+Module: %s' % obj.__name__)
        funcs = []
        for name in obj.__dict__:
            item = getattr(obj, name)
            if inspect.ismethod(item) or inspect.isfunction(item) or inspect.isroutine(item):
                # self.skip_func(item, True)
                funcs.append(name)
        return funcs

    def class_funcs(self, obj):
        """ ModuleFunc the class object passed as argument,
        including its methods """

        print('+Class: %s' % obj.__name__)
        funcs = []
        for name in obj.__dict__:
            item = getattr(obj, name)
            if inspect.ismethod(item) or inspect.isroutine(item) or inspect.ismethod(item):
                # self.skip_func(item, True)
                funcs.append(name)
            if inspect.isdatadescriptor(item):
                funcs.append(name)
        return funcs

    def describe(self, module):
        """ ModuleFunc the module object passed as argument
        including its classes and functions """

        print('[Module: %s]\n' % module.__name__)

        for name in dir(module):
            obj = getattr(module, name)
            if inspect.isclass(obj):
                self.class_funcs(obj)
            elif (inspect.ismethod(obj) or inspect.isfunction(obj)):
                self.skip_func(obj)
            elif inspect.isbuiltin(obj):
                self.skip_builtin(obj)
            else:
                print name

        print('(No members)')


class FileInfo(object):
    """
    Get import/Class/func and calling functions held in dict
    """

    def __init__(self, pfile, pkg_name):
        self.pfile = os.path.abspath(pfile)
        self.pkg_name = pkg_name

    @property
    def dirname(self):
        return os.path.dirname(self.pfile)

    def get_module_name(self):
        module_name = os.path.basename(self.pfile)
        module_name = module_name.replace('.py', '')
        return module_name

    @property
    def module_name(self):
        return self.get_module_name()

    def get_module_name_long(self):
        module_name = self.get_module_name()
        items = self.dirname.split('/')
        index = items.index(self.pkg_name)
        eles = items[index:]
        eles.append(module_name)
        return '.'.join(eles)

    def dm_info(self):
        """
        Module/Class Information by importing the module
        """
        dm = {}
        # module name to module
        module = importlib.import_module(self.get_module_name_long(), package=self.pkg_name)
        mf = ModuleFunc()
        dm[self.module_name] = mf.module_funcs(module)

        # import module
        # get class functions
        df = self.df_info()
        classes = df.get('classes', [])
        for cls_name in classes:
            obj = getattr(module, cls_name)

            dm[cls_name] = mf.class_funcs(obj)

        return dm

    def df_info(self):
        """
        To get some basic information by reading file
        import -- to figure out module/class name of the corresponding module if it is test module
        module name of the self.pfile
        class names of the self.pfile
        module functions of the self.pfile

        each class functions of the self.pfile -- will be got by loading the module
        It is difficult to figure out function contains/called in each test func?! to match module/class/function

        :rtype: dict
        """
        d = {}
        if not os.path.isfile(self.pfile):
            return
        d['dirname'] = self.dirname
        d['module_name'] = self.module_name
        d['module_name_long'] = self.get_module_name_long()
        print self.pfile
        with open(self.pfile, 'r') as fd:
            for line in fd:
                d = self.line_handling(line, d)
        return d

    def line_handling(self, line, d):
        """
        Update dict from one line
        """
        if not line:
            return d
        line = line.rstrip()
        cls_name = self.is_cls(line)
        if cls_name:
            # d_func_code = {}
            d[cls_name] = {}
            l_cls = d.get('classes', [])
            l_cls.append(cls_name)
            d['classes'] = l_cls
            d['cls_now'] = cls_name
            return d

        module_func = self.is_module_func(line)
        if module_func:
            l_module_func = d.get(self.module_name, [])
            l_module_func.append(module_func)
            d[self.module_name] = l_module_func
            return d

        func = self.is_func(line)
        if func:
            d['func_now'] = func
            return d

        imp = self.is_import(line)
        if imp:
            l_import = d.get('import', [])
            if line not in l_import:
                l_import.append(line)
                d['import'] = l_import
            import_name = self.import_name(line)
            if import_name:
                l_import_name = d.get('import_name', [])
                l_import_name.append(import_name)
                d['import_name'] = l_import_name
            return d

        cls_now = d.get('cls_now', None)
        func_now = d.get('func_now', None)

        if not cls_now:
            return d

        if not func_now:
            return d

        line = line.lstrip()
        if len(line) < 3:
            return d

        if '@' in line:
            return d

        d_func_code = d.get(cls_now, {})
        l_func_code = d_func_code.get(func_now, [])
        l_func_code.append(line)
        d_func_code[func_now] = l_func_code
        d[cls_now] = d_func_code
        return d

    def is_cls(self, line):
        if not line.startswith('class '):
            return False
        items = line.split(' ')
        second = items[1]
        items = second.split('(')
        return items[0]

    def is_module_func(self, line):
        if not line.startswith('def '):
            return False
        items = line.split('def ')
        second = items[1]
        items = second.split('(')
        return items[0]

    def is_func(self, line):
        if ' def ' not in line:
            return False
        items = line.split('def ')
        second = items[1]
        items = second.split('(')
        return items[0]

    def is_import(self, line):
        if 'import ' not in line:
            return False
        return line

    def import_name(self, import_line):
        # assume it is not this pkg
        if import_line.startswith('import'):
            return None
        items = import_line.split(' ')
        return items.pop()


class MatchMaking(object):

    def __init__(self, argv):
        self.argv = argv
        args, extra = self.init_args()
        self.args = args
        self.extra = extra

    def init_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--run', type=bool, default=False, help='do not do anything for now')
        parser.add_argument('--pkg_name', type=str, default='quiz', help='Package Name')
        args, extra = parser.parse_known_args(self.argv)
        return args, extra

    @property
    def pkg_name(self):
        return self.args.pkg_name

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
                        if fname.startswith('test_'):
                            fpath = os.path.join(root_dir, dirName, fname)
                            lp.append(fpath)
        return lp

    def get_files(self):
        if not self.extra:
            return []
        items = []
        for item in self.extra:
            if item.endswith('.py'):
                items.append(item)

        return items

    def match(self):
        items = self.get_files()

        if not items:
            return
        if len(items) == 2:
            pass
        else:
            line = '1 test and 1 being tested python file required'
            print line
            return
        test_file = items[0]
        being_tested = items[1]

        fi_test = FileInfo(test_file, self.pkg_name)
        df_test = fi_test.df_info()
        pprint(df_test)
        dm_test = fi_test.dm_info()
        pprint(dm_test)

        fi = FileInfo(being_tested, self.pkg_name)
        df = fi.df_info()
        pprint(df)
        dm = fi.dm_info()
        pprint(dm)

        test_classes = df_test.get('classes', [])
        for test_cls in test_classes:
            self.match_test_cls(test_cls, df_test, dm, df)

    def match_test_cls(self, test_cls, df_test, dm, df):
        print test_cls
        test_funcs = df_test.get(test_cls, [])
        d_func_code = df_test.get(test_cls, {})
        import_name = df_test.get('import_name', [])
        module = df.get('module_name', None)
        # module or class name held in dm
        keys = dm.keys()
        # import not always works if import *
        print 'Source Module {0} imported by {1}'.format(keys, import_name)
        d_matched = {}
        d_missing = {}
        for key in keys:
            # key could be module/class
            module_functions = dm.get(key, [])
            for func in module_functions:
                match = False
                for test_func in test_funcs:
                    l_func_code = d_func_code.get(test_func, [])
                    for line_code in l_func_code:
                        if '.{0}'.format(func) in line_code:
                            value = [key, func]
                            if key not in import_name:
                                value = [module, key, func]

                            d_matched[test_func] = value
                            match = True
                if not match:
                    d_missing[func] = key

        print "\n\n*** Not tested"
        pprint(d_missing)
        print "\n\n*** Test Match"
        keys = d_matched.keys()
        for key in keys:
            value = '.'.join(d_matched.get(key, []))
            line = '        \'{}\': {}'.format(key, value)
            print line


def main(argv):
    fm = MatchMaking(argv)
    fm.match()


if __name__ == '__main__':
    main(sys.argv[1:])
