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

# logger for the module
logger = logging.getLogger('quiz')

class Quiz(object):
    # could use *args
    def __init__(self, category):
        self.category = category
        # logger for the class
        self.logger = logging.getLogger('quiz.Quiz')
        self.logger.info('creating an instance of Quiz')
    def square(self, x):
        self.logger.info('square')
        return x*x

    def print_args(self, x):
        self.logger.info('print_args')
        print x

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

    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

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

