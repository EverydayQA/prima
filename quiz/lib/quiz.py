#!/usr/bin/python
import json
import simplejson
import sys
import os
from pprint import pprint
import logging
import menu

# Quiz base class/subclass
# add *args, **kwargs - all unittest for common usae
# logger for the module
logger = logging.getLogger('quiz')

class Quiz(object):
    # could use *args
    def __init__(self, args, kwargs):
        if kwargs.get['category']:
            self.category = kwargs['category']
        else:
            self.category = 'QA'
        # logger for the class
        self.logger = logging.getLogger('quiz.Quiz')
        self.logger.info('creating an instance of Quiz')

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
        
    def jason_2_dict(self):
        pass
    def txt_2_dict(self):
        pass
    def dict_2_jason(self):
        pass
    def dict_2_txt(self):
        pass

class QuizQA(Quiz):
    # could use (*args, **kwargs)
    # or (category, **kwargs)
    def __init__(self, category, *args, **kwargs):
        super(QuizQA, self).__init__(category)
        # logger for the class - logging level from kwargs?
        self.logger = logging.getLogger('quiz.QuizQA')
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

    # arguments from self or (*args, **kwargs)
    def print_args(self,x, *args, **kwargs):
        super(QuizQA, self).print_args(x)
        self.logger.info(args)
        self.logger.info(kwargs)


class QuizList(object):
    def __init__(self, args, kwargs):
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

def full_name_class(cls):
    return cls.__module__ + "." + cls.__class__.__name__

def full_name_func():
    file_name = os.path.basename(__file__)
    func_name = full_name_func.__name__
    print file_name
    print func_name

def main():    
    categories = ['QC', 'python']
    category = menu.select_from_list(categories)

    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    qz = Quiz(category)
    name_cls = full_name_class(qz)
    logger.info(name_cls)

    qz.print_args('ok')

    args = ['a','b','c']
    sample_dict = {'aaa':1, 'ccc':3}

    qza = QuizQA(category, 1, *args, **sample_dict)
    qza.print_args('xxxx','aa','abbb',val='va',bbb='xxx')

    full_name_func()
if __name__ == '__main__':
    main()

