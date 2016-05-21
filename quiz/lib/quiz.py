#!/usr/bin/python
import json
import simplejson
import sys
import os
from pprint import pprint
import logging
import menu
import inspect
import argparse
# Quiz base class/subclass
# add *args, **kwargs - all unittest for common usae
# logger for the module
logger = logging.getLogger(__name__)

class Quiz(object):
    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)
        self.logger.propagate = False    
        el  = self.logger.getEffectiveLevel()
        print '\nlogger level is: {0} args cls {1} EffectiveLevel {2}\n'.format(self.logger.level, self.__class__.__name__, el)

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
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)
        self.logger.propagate = False    
        el  = self.logger.getEffectiveLevel()
        print '\nlogger level is: {0} args cls {1} EffectiveLevel {2}\n'.format(self.logger.level, self.__class__.__name__, el)

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
        self.logger.debug(x)
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
    parser.add_argument("-logging", '--logging', type=int, default=30, dest='logging', help='logging level 0 10 20')
    parser.add_argument('-files', nargs='*')
    args = parser.parse_args()
    return args

def get_full_class_name(cls):
    return cls.__module__ + "." + cls.__class__.__name__

def get_full_func_name():
    file_name = os.path.basename(__file__)
    func_name = get_full_func_name.__name__
    func_name = inspect.stack()[0][3]
    return func_name

def main():    
    args = init_args_quiz_outside_class()
    categories = ['QC', 'python']
    category = menu.select_from_list(categories)

    logger.setLevel(args.logging)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(args.logging)
    el  = logger.getEffectiveLevel()
    print '\nlogger level is: {0} args logging {1} EffectiveLevel {2}\n'.format(logger.level, args.logging, el)
    # std_formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    # prevent duplicate logging
    logger.propagate = True  

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

