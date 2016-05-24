#!/usr/bin/python
import os
import json
import simplejson
import sys
import logging
import menu
import argparse
from quiz_logger import QuizLogger
from quiz import Quiz
from color_print import ColorPrint
from random import randint
from parse_json import ParseJson

class AddQuiz(object):
    def __init__(self, *args, **kwargs):
        # default level is 20 in case not defined
        self.args = args
        self.kwargs = kwargs
        name = __name__ + "." + self.__class__.__name__
        self.logger = QuizLogger(name=name, level=10).logger
        self.logger.info('__init__()')
        self.logger.info(self.args)
        self.logger.info(kwargs)
        self.quizid = self.kwargs.get('quizid')

    def set_category(self):
        self.category = self.kwargs.get('category')
        if not self.category:
            self.category = self.prompt('Please add or select a category')
            self.logger.info('prompt_category')
        return self.category
    def set_description(self):
        desc = self.prompt('add desc')
        return desc
    def set_quality(self):
        return 50
    def set_weight(self):
        return 1
    def set_quizid(self):
        if self.quizid:
            pass
        else:
            int_random = randint(111,999)
            self.quizid = int_random
        return int_random
    def set_level(self):
        self.level = self.kwargs.get('level')
        if self.level:
            pass
        else:
            self.level = 1
        return self.level

    def set_answers(self):
        ans = []
        input_str = self.prompt('add correct answer(s), separated by space')
        ans = input_str.split(' ')
        return ans

    def set_questions(self):
        questions = []
        for i in range(4):
            que = self.prompt('add a few questions')
            questions.append(que)
        return questions

    def prompt(self, str):
        print str
        input = raw_input()
        return input
    def set_quiz_dict(self):
        quiz_dict = {}

        quiz_dict['category'] = self.set_category()
        quiz_dict['quizid'] = self.set_quizid()
        quiz_dict['description'] = self.set_description()
        question = self.set_questions()
        quiz_dict['questions'] = question
        ans = self.set_answers()
        quiz_dict['answers'] = ans
        return quiz_dict

def init_args_add_quiz():
    parser = argparse.ArgumentParser()
    parser.add_argument('--logging', type=int, default=20, help='logging level')
    parser.add_argument('--category', type=str, default='QC', help='Category')

    args, args_extra = parser.parse_known_args(sys.argv[1:] )
    return args, args_extra

def main():    
    args, args_extra = init_args_add_quiz()

    log = QuizLogger(name=__file__,level=logging.INFO, logname='/tmp/test2.log')
    
    cp = ColorPrint()
    cstr = cp.cstr('logging color string', cp.RED)
    log.logger.info(cstr)
    kwargs = vars(args)
    # extra args as args, while args serves as kwargs for class AddQuiz
    add_quiz = AddQuiz(args_extra, **vars(args))
    quiz_dict = add_quiz.set_quiz_dict()
    log.logger.info(quiz_dict)

    quizid = add_quiz.quizid
    level  = add_quiz.set_level()
    file_to_write = add_quiz.category + '_' + level + '_' + str(quizid) + '.json'
    # write to data base - filename?
    pjson = ParseJson()
    data_dir = pjson.data_dir
    file_to_write  = os.path.join(data_dir, file_to_write)
    pjson.dict2json(quiz_dict, file_to_write)
    qz = pjson.dict2quiz(quiz_dict)
    sels = qz.multiple_choices()
    log.logger.info(sels)

    ans = qz.answers
    log.logger.info(ans)

    result = qz.quiz_result(sels)
    log.logger.info(result)

if __name__ == '__main__':
    main()

