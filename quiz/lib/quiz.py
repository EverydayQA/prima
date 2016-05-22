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
# logger propagate example
class Quiz(object):
    def __init__(self, *args, **kwargs):
        # logger name has to be this way to alow propagate EffetiveLeve
        name = __name__ + "." + self.__class__.__name__
        self.logger = logging.getLogger(name)
        # this is necessary to pass logger handler to subclass?
        self.logger.propagate = True    
        el  = self.logger.getEffectiveLevel()
        line = 'logger level is: {0} args cls {1} EffectiveLevel {2}\n'.format(self.logger.level, name, el)
        self.logger.debug(line)
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
        self.logger.info(self.args )
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
        name = __name__ + "." + self.__class__.__name__
        self.logger.info('self.logger alreay defined in base class {0}'.format(name) )
        #self.logger = logging.getLogger(name)
        el  = self.logger.getEffectiveLevel()
        line = 'logger level is: {0} args cls {1} EffectiveLevel {2}\n'.format(self.logger.level, name, el)
        self.logger.debug(line)
        self.args = args
        self.kwargs = kwargs

    def print_args(self, x):
        super(QuizQA, self).print_args()
        print x
        self.logger.debug(x)


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

def init_args():    
    # argument may vary
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-?", '--help', action="help",help='xxx')
    parser.add_argument("-category", '--category', type=str, default=None, dest='category', help='category')

    parser.add_argument("-run", '--run', action='store_true', dest='run', help='run')
    parser.add_argument("-logging", '--logging', type=int, default=30, dest='logging', help='logging level 0 10 20')
    parser.add_argument('-files', nargs='*')
    args, args_extra = parser.parse_known_args()
    return args, args_extra

def get_full_class_name(cls):
    return cls.__module__ + "." + cls.__class__.__name__

def get_full_func_name():
    file_name = os.path.basename(__file__)
    func_name = get_full_func_name.__name__
    func_name = inspect.stack()[0][3]
    return func_name

def main():    

    args, args_extra = init_args()
    logger = logging.getLogger(__name__)

    logger.setLevel(args.logging)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(args.logging)
    el  = logger.getEffectiveLevel()
    line = 'logger level is: {0} args logging {1} EffectiveLevel {2}\n'.format(logger.level, args.logging, el)
    logger.debug(line)
    # std_formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    # prevent duplicate logging
    logger.propagate = True  

    logger.info(args)
    logger.info(args_extra)

    logger.info('This is only for development!')

    qz = Quiz(*args_extra, **vars(args) )
    cls_name = get_full_class_name(qz)
    logger.info('class_name: {0}'.format(cls_name) )
    qz.print_args()

    qza = QuizQA(*args_extra, **vars(args) )
    cls_name = get_full_class_name(qza)
    logger.info('class_name: {0}'.format(cls_name) )
    qza.print_args('func with exta parameters!')

    args = ['a','b','c']
    sample_dict = {'aaa':1, 'ccc':3}


if __name__ == '__main__':
    main()

