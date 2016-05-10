#!/usr/bin/python
import json
import simplejson
import sys
from pprint import pprint
import logging
import menu

# time allocated - 2 hours
# Quiz base class/subclass
# add *args, **kwargs - all unittest for common usae

class Quiz(object):
    # could use *args
    def __init__(self, category):
        self.category = category
        print "QuizBase"
    def square(self, x):
        return x*x

    def print_args(self, x):
        print x

class QuizQA(Quiz):
    # could use (*args, **kwargs)
    # or (category, **kwargs)
    def __init__(self, category, *args, **kwargs):
        super(QuizQA, self).__init__(category)
        self.args = args
        self.kwargs = kwargs

    # or use to init class directly
    def init_args_quiz_inside_class():    
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument("-?", '--help', action="help",help='xxx')
        parser.add_argument("-category", '--category', type=str, default=None, dest='category', help='category')

        parser.add_argument("-run", '--run', action='store_true', dest='run', help='run')
        parser.add_argument("-logging", '--logging', type=int, default=20, dest='logging', help='logging level 0 10 20')
        parser.add_argument('-files', nargs='*')
        args = parser.parse_args()
        return args

    # arguments from self or (*args, **kwargs)
    def print_args(self,x, *args, **kwargs):
        # 
        super(QuizQA, self).print_args(x)
        print self.args
        print self.kwargs

        for arg in args:
            print arg
        print kwargs

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

def main():    
    # choose category
    categories = ['QC', 'python']
    category = menu.select_from_list(categories)
    logger = logging.getLogger('quiz')
    logger.addHandler(logging.StreamHandler() )
    logger.setLevel(logging.DEBUG)
    print logging.INFO
    print logging.DEBUG
    logger.info('1 - info')
    logger.debug('2 - debug should not haapen as level is info')
    
    qz = Quiz(category)
    qz.print_args('ok')

    args = ['a','b','c']
    sample_dict = {'aaa':1, 'ccc':3}

    qza = QuizQA(category, 1, *args, **sample_dict)
    qza.print_args('xxxx','aa','abbb',val='va',bbb='xxx')

if __name__ == '__main__':
    main()

