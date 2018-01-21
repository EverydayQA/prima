import argparse
import sys
import os
from pprint import pprint
import pkgutil
import inspect
import importlib


class Describe(object):

    def __init__(self):
        pass

    def describe_builtin(self, obj):
        """ Describe a builtin function """
        print('+Built-in Function: %s' % obj.__name__)

    def describe_func(self, obj, method=False):
        """ Describe the function object passed as argument.
        If this is a method object, the second argument will
        be passed as True """

        if method:
            print('+Method: %s' % obj.__name__)
        else:
            print('+Function: %s' % obj.__name__)

    def describe_klass(self, obj):
        """ Describe the class object passed as argument,
        including its methods """

        print('+Class: %s' % obj.__name__)

        for name in obj.__dict__:
            item = getattr(obj, name)
            if inspect.ismethod(item):
                self.describe_func(item, True)

        print

    def describe(self, module):
        """ Describe the module object passed as argument
        including its classes and functions """

        print('[Module: %s]\n' % module.__name__)

        for name in dir(module):
            obj = getattr(module, name)
            if inspect.isclass(obj):
                self.describe_klass(obj)
            elif (inspect.ismethod(obj) or inspect.isfunction(obj)):
                self.describe_func(obj)
            elif inspect.isbuiltin(obj):
                self.describe_builtin(obj)
            else:
                print name

        print('(No members)')


class ModuleInfo(object):

    def __init__(self, module_name, pkg_name):
        self.module_name = module_name
        self.pkg_name = pkg_name
        self.dsc = Describe()

    def cls_funcs(self, module_name):
        # module = __import__(module_name, fromlist=[self.pkg_name])
        module = importlib.import_module(module_name, package=self.pkg_name)

        for element_name in dir(module):
            element = getattr(module, element_name)
            print("other {} {}".format(element_name, dir(element)))

    def element_cls_dir(self, module_name):
        # module = __import__(module_name, fromlist=['quiz'])
        module = importlib.import_module(module_name)

        items = []
        for element_name in dir(module):
            element = getattr(module, element_name)
            if inspect.isclass(element):
                print("class {} {}".format(element_name, module))
                items.append(element)
                qname = '{0}.{1}'.format(module_name, element_name)
                # self.dsc.describe(module)

        return items

    def explore_package(self, module_name):
        self.element_cls_dir(module_name)
        loader = pkgutil.get_loader(module_name)
        all_packages = pkgutil.walk_packages([loader.filename])
        for sub_module in all_packages:
            _, sub_module_name, _ = sub_module
            qname = module_name + "." + sub_module_name
            print(qname)
            # self.element_cls_dir(qname)
            self.dsc.describe(sub_module)
            self.explore_package(qname)

    def inspect_package(self, package_name):
        module = __import__(package_name, fromlist=['quiz'])
        # importlib.import_module('.c', 'a.b')
        # importlib.import_module('a.b.c')
        for element_name in dir(module):
            element = getattr(module, element_name)
            if inspect.isclass(element):
                print("class %s" % element_name)
            elif inspect.ismodule(element):
                pass
            elif hasattr(element, '__call__'):
                if inspect.isbuiltin(element):
                    sys.stdout.write("builtin_function %s" % element_name)
                    print("")
                else:
                    try:
                        data = inspect.getargspec(element)
                        sys.stdout.write("function %s" % element_name)
                        for a in data.args:
                            sys.stdout.write(" ")
                            sys.stdout.write(a)
                        if data.varargs:
                            sys.stdout.write(" *")
                            sys.stdout.write(data.varargs)
                            print("")
                    except Exception:
                        pass
                    else:
                        print("value %s" % element_name)


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

    def get_module_name_short(self):
        module_name = os.path.basename(self.pfile)
        module_name = module_name.replace('.py', '')
        return module_name

    @property
    def module_name(self):
        return self.get_module_name_short()

    def get_module_name_long(self):
        module_name = self.get_module_name_short()
        items = self.dirname.split('/')
        index = items.index(self.pkg_name)
        eles = items[index:]
        eles.append(module_name)
        return '.'.join(eles)

    def d_minfo(self):
        """
        Module/Class Information by importing the module
        """
        d = {}

        return d

    def d_finfo(self):
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
        print self.pfile
        with open(self.pfile, 'r') as fd:
            for line in fd:
                d = self.line_handling(line, d)

        # minfo = ModuleInfo('add_quiz', 'quiz')
        # minfo.inspect_package('quiz.add.add_quiz')
        # minfo.explore_package('quiz.add.add_quiz')
        return d

    def line_handling(self, line, d):
        """
        Update dict from one line
        """
        if not line:
            return d
        line.rstrip()
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
            l_module_func = d.get(self.moduel_name, [])
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
            return d

        cls_now = d.get('cls_now', None)
        func_now = d.get('func_now', None)

        if not cls_now:
            return d

        if not func_now:
            return d

        line = line.replace(' ', '')
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
        imp = line.strip('\n')
        return imp

    def module_name_import(self, import_line):
        if self.pkg_name in import_line:
            pass


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
        if not self.get_files():
            return
        for item in self.get_files():
            fi = FileInfo(item, self.pkg_name)
            d = fi.d_finfo()
            pprint(d)
            module_name = fi.get_module_name_long()
            module_name_short = fi.get_module_name_short()
            print module_name
            print module_name_short


def main(argv):
    fm = MatchMaking(argv)
    fm.match()


if __name__ == '__main__':
    main(sys.argv[1:])
