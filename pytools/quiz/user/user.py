import os
import inspect
import argparse


class User(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @property
    def login(self):
        alogin = self.kwargs.get('login', 'invalid')
        return alogin

    @property
    def password(self):
        apw = self.kwargs.get('password', 'invalid')
        return apw

    @property
    def email(self):
        mail = self.kwargs.get('email', 'invalid')
        return mail

    @property
    def userid(self):
        uid = self.kwargs.get('userid', 'invalid')
        return uid


class Taker(User):

    def __init__(self, *args, **kwargs):

        self.category = kwargs.get('category', 'QA')
        super(Taker, self).__init__(args, kwargs)
        self.args = args
        self.kwargs = kwargs


def init_args():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-?", '--help', action="help", help='xxx')
    parser.add_argument("-category", '--category', type=str, default=None, dest='category', help='category')

    parser.add_argument("-run", '--run', action='store_true', dest='run', help='run')
    parser.add_argument("-logging", '--logging', type=int, default=30, dest='logging', help='logging level 0 10 20')
    args, args_extra = parser.parse_known_args()
    return args, args_extra


def get_full_class_name(cls):
    return cls.__module__ + "." + cls.__class__.__name__


def get_full_func_name():
    file_name = os.path.basename(__file__)
    print(file_name)
    func_name = get_full_func_name.__name__
    func_name = inspect.stack()[0][3]
    return func_name


def main():
    args, args_extra = init_args()

    aper = User(*args_extra, **vars(args))
    cls_name = get_full_class_name(aper)
    taker = Taker(*args_extra, **vars(args))
    cls_name = get_full_class_name(taker)
    print(cls_name)


if __name__ == '__main__':
    main()
