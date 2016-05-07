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

    # arguments from self or (*args, **kwargs)
    def print_args(self,x, *args, **kwargs):
        # 
        super(QuizQA, self).print_args(x)
        print self.args
        print self.kwargs

        for arg in args:
            print arg
        print kwargs

def main():    
    # choose category
    categories = ['QC', 'python']
    category = menu.select_from_list(categories)
    
    qz = Quiz(category)
    qz.print_args('ok')

    args = ['a','b','c']
    sample_dict = {'aaa':1, 'ccc':3}

    qza = QuizQA(category, 1, *args, **sample_dict)
    qza.print_args('xxxx','aa','abbb',val='va',bbb='xxx')

if __name__ == '__main__':
    main()

