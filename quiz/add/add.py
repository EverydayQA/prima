#!/usr/bin/python
import os
import json
import simplejson
import sys
import logging
import argparse
from random import randint

import add_quiz
from quiz import menu
from quiz.quiz_logger import QuizLogger
from quiz.color_print import ColorPrint
from quiz.parse_json import ParseJson


def init_args_addquiz():
    parser = argparse.ArgumentParser()
    parser.add_argument('--logging', type=int, default=20, help='logging level')
    parser.add_argument('--category', type=str, default='QC', help='Category')

    args, args_extra = parser.parse_known_args(sys.argv[1:] )
    return args, args_extra

def main():    
    args, args_extra = init_args_addquiz()
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
    print cstr
    kwargs = vars(args)
    # extra args as args, while args serves as kwargs for class AddQuiz
    addquiz = add_quiz.AddQuiz(args_extra, **vars(args))
    quiz_dict = addquiz.set_quiz_dict()
    logger.info(quiz_dict)

    quizid = addquiz.quizid
    level  = addquiz.set_level()

    file_to_write = addquiz.category + '_' + str(level) + '_' + str(quizid) + '.json'

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

