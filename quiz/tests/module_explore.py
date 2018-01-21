import importlib
from .match_make import ModuleFunc
import inspect
import pkgutil
import pprint
import sys


class ModuleInfo(object):

    def __init__(self, module_name, pkg_name):
        self.module_name = module_name
        self.pkg_name = pkg_name
        self.dsc = ModuleFunc()

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


