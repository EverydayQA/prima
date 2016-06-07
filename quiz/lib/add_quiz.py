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

        self.quizid = self.kwargs.get('quizid')
    @property
    def logger(self):
        name = os.path.splitext(os.path.basename(__file__))[0] + "." + self.__class__.__name__ 
        logger = logging.getLogger(name)
        log_level = self.kwargs.get('log_level', 30)
        logger.setLevel(log_level)
        el  = logger.getEffectiveLevel()
        line = 'logger level is: {0} args cls {1} EffectiveLevel {2}\n'.format(logger.level, name, el)
        logger.debug(line)
        return logger 

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
        input_str = None
        while not input_str:
            print str
            input_str = raw_input()
            
        return input_str
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
    name = os.path.splitext(os.path.basename(__file__))[0]
    logger = logging.getLogger(name)

    logger.setLevel(args.logging)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(args.logging)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.propagate = False
     
    cp = ColorPrint()
    cstr = cp.cstr('logging color string', cp.RED)
    logger.info(cstr)
    kwargs = vars(args)
    # extra args as args, while args serves as kwargs for class AddQuiz
    add_quiz = AddQuiz(args_extra, **vars(args))
    quiz_dict = add_quiz.set_quiz_dict()
    logger.info(quiz_dict)

    quizid = add_quiz.quizid
    level  = add_quiz.set_level()

    file_to_write = add_quiz.category + '_' + str(level) + '_' + str(quizid) + '.json'

    # write to file/not sql
    pjson = ParseJson()
    data_dir = pjson.data_dir
    file_to_write  = os.path.join(data_dir, file_to_write)
    pjson.dict2json(quiz_dict, file_to_write)
    qz = pjson.dict2quiz(quiz_dict)

    sels = qz.multiple_choices()
    logger.info(sels)

    ans = qz.answers
    logger.info(ans)

    result = qz.quiz_result(sels)
    logger.info(result)

if __name__ == '__main__':
    main()

