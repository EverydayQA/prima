#!/usr/bin/python
import os
import json
import simplejson
import sys
from pprint import pprint
import logging
import menu
import argparse
from quiz_logger import QuizLogger
from quiz import Quiz
from color_print import ColorPrint
# this example will demo
# logging
# argparse - extra args
# args and kwargs

# must be (cls,cls) not(object, cls)
class AddQuiz(object):
    def __init__(self, *args, **kwargs):
        if kwargs.get('category'):
            self.category = kwargs['category']
        else:
            self.cagegory = 'QC'
        self.args = args
        self.logger = QuizLogger(name=self.__class__.__name__, level=logging.INFO).logger
        self.logger.info('__init__()')
    def add_question(self):
        file_add = file_to_write()    
        sample_dict = {'aaa':1, 'ccc':3}
        self.logger.info('add_question')
        # self.category
        # file_name - to be decided later on by a function
        # multiple choices format using either XML or Jason
        write_dict_to_json(sample_dict, file_add)

        # png/jpg/gif
        return 8;
    def file_to_write(self):
        file_base = '333.json'
        data_dir = '/tmp'
        file_new = os.path.join(data_dir, file_base)
        return file_new

    def read_json(self, file_json):
        data_list = []
        with open(file_json, 'r') as f:
            data_list = json.load(f)

        return data_list    

    def write_dict_to_json(self, data_dict, file_json):
        d = {"name":"interpolator", \
             "children":[{'name':key,"size":value} \
             for key,value in data_dict.items()]}

        with open(file_json, 'w') as f:
            j = json.dumps(d, indent=4)
            print >> f, j
            f.close()

def init_args_add_quiz():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo')
    args, args_extra = parser.parse_known_args(sys.argv[1:] )
    return args, args_extra

def main():    
    args, args_extra = init_args_add_quiz()

    log = QuizLogger(name=__file__,level=logging.INFO)
    log.logger.info(args)
    log.logger.info(args_extra)
    
    cp = ColorPrint()
    color_string = cp.color_string('logging color string', cp.RED)
    log.logger.error(color_string)
    add_quiz = AddQuiz(args_extra, category='QC', logging=10)
    json2write = add_quiz.file_to_write()

    # ways to add
    # from existing files with different format --> converted to json
    # from input -> convert to dict
    # from dict ()
    sample_dict = {'aaa':1, 'ccc':3}

    add_quiz.write_dict_to_json(sample_dict, json2write)

    # read a json file
    data_list = add_quiz.read_json(json2write)


    log.logger.info(data_list)
    log.logger.info(add_quiz.args)

if __name__ == '__main__':
    main()

