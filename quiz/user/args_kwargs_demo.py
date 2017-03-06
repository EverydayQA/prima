#!/usr/bin/python
import sys
import os
import logging
import argparse


class User(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.print_args_kwargs()
    @property
    def logger(self):
        name = __name__ + "." + self.__class__.__name__
        logger = logging.getLogger(name)
        logger.propagate = True    
        el  = logger.getEffectiveLevel()
        return logger
        
    def set_exam(self):
        exam = Exam(*self.args, **self.kwargs)

    def print_args_kwargs(self):
        self.logger.info('User {0} {1} {2} {3}'.format(type(self.args), type(self.kwargs), self.args, self.kwargs))

class Exam(object):               
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.print_args_kwargs()
     
    @property
    def logger(self):
        name = __name__ + "." + self.__class__.__name__
        logger = logging.getLogger(name)
        logger.propagate = True    
        el  = logger.getEffectiveLevel()
        return logger

    def print_args_kwargs(self):
        self.logger.info('Exam {0} {1} args: {2} kwargs: {3}'.format(type(self.args), type(self.kwargs), self.args, self.kwargs))
        

def init_args():    
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-?", '--help', action="help",help='xxx')
    parser.add_argument("-category", '--category', type=str, default=None, dest='category', help='category')
    parser.add_argument("-run", '--run', action='store_true', dest='run', help='run')
    parser.add_argument("-logging", '--logging', type=int, default=30, dest='logging', help='logging level 0 10 20')
    args, args_extra = parser.parse_known_args()
    return args, args_extra

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

    logger.info('main() {0} {1} {2} {3}'.format(type(args), type(args_extra), args, args_extra))

    aper = User(*args_extra, **vars(args) )
    aper.set_exam()

if __name__ == '__main__':
    main()

