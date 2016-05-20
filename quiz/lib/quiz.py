#!/usr/bin/python
import json
import simplejson
import sys
import os
from pprint import pprint
import logging
import menu
import inspect

# Quiz base class/subclass
# add *args, **kwargs - all unittest for common usae
# logger for the module
logger = logging.getLogger('quiz')

class Quiz(object):
    def __init__(self, *args, **kwargs):
        name = __name__ + '.' + self.__class__.__name__
        self.logger = logging.getLogger(name)
        self.logger.info('creating an instance of Quiz')
        self.args = args
        self.kwargs = kwargs
    @property
    def questions(self, qdict):
        self.questions = qdict
        return self.questions

    @property
    def answers(self, adict):
        self.answers = adict
        return self.answers

    def print_args(self):
        self.logger.info(self.args)
        self.logger.info(self.kwargs)
        
    def jason_2_dict(self):
        pass
    def txt_2_dict(self):
        pass
    def dict_2_jason(self):
        pass
    def dict_2_txt(self):
        pass

class QuizQA(Quiz):
    def __init__(self, *args, **kwargs):
        self.category = kwargs.get('category','QA')
        super(QuizQA, self).__init__(args, kwargs)
        name = __name__ + '.' + self.__class__.__name__
        self.logger = logging.getLogger(name)
        self.logger.info('creating an instance of QuizQA')

        self.args = args
        self.kwargs = kwargs
        self.logger.info(args)
        self.logger.info(kwargs)

    # or use to init class directly
    def init_args_quiz_inside_class():    
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument("-?", '--help', action="help",help='xxx')
        parser.add_argument("-category", '--category', type=str, default=None, dest='category', help='category')

        parser.add_argument("-run", '--run', action='store_true', dest='run', help='run')
        parser.add_argument("-logging", '--logging', type=int, default=20, dest='logging', help='logging level 0 10 20')
        parser.add_argument('-files', nargs='*')
        args = parser.parse_args()
        self.logger.info(args)
        return args

    def print_args(self, x):
        super(QuizQA, self).print_args()
        print x
        self.logger.info(self.args)
        self.logger.info(self.kwargs)


class QuizList(object):
    def __init__(self, *args, **kwargs):
       self.args = args
       self.kwargs = kwargs
    def add_item(self, item):
        pass
    def remove_item(self, item):
        pass
    def modify_item(self, item):
        pass
    def display_list(self):
        pass

def init_args_quiz_outside_class():    
    # argument may vary
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-?", '--help', action="help",help='xxx')
    parser.add_argument("-category", '--category', type=str, default=None, dest='category', help='category')

    parser.add_argument("-run", '--run', action='store_true', dest='run', help='run')
    parser.add_argument("-logging", '--logging', type=int, default=20, dest='logging', help='logging level 0 10 20')
    parser.add_argument('-files', nargs='*')
    args = parser.parse_args()
    return args

def get_full_class_name(cls):
    return cls.__module__ + "." + cls.__class__.__name__

def get_full_func_name():
    file_name = os.path.basename(__file__)
    func_name = get_full_func_name.__name__
    func_name = inspect.stack()[0][3]
    logger.info( func_name )
    return func_name

def main():    
    categories = ['QC', 'python']
    category = menu.select_from_list(categories)

    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)

    # std_formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    qz = Quiz()
    cls_name = get_full_class_name(qz)
    logger.info('class_name: {0}'.format(cls_name) )

    qz.print_args()

    args = ['a','b','c']
    sample_dict = {'aaa':1, 'ccc':3}

    qza = QuizQA()
    qza.print_args('xxx')

    func = get_full_func_name()
    logger.info(func)
if __name__ == '__main__':
    main()

