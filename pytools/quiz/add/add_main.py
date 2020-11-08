#!/usr/bin/python
import os
import sys
import logging
import argparse
from random import randint
from quiz.lib import quiz_name

import add_quiz
from quiz.lib import menu
from quiz.lib.parse_json import ParseJson


def init_args_addquiz():
    parser = argparse.ArgumentParser()
    parser.add_argument('--logging', type=int, default=20, help='logging level')
    parser.add_argument('--category', type=str, default='QC', help='Category')

    args, args_extra = parser.parse_known_args(sys.argv[1:])
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

    kwargs = vars(args)
    # extra args as args, while args serves as kwargs for class AddQuiz
    addquiz = add_quiz.AddQuiz(args_extra, **vars(args))
    quiz_dict = addquiz.set_quiz_dict()
    logger.info(quiz_dict)

    quizid = addquiz.quizid
    level = addquiz.set_level()

    quizName = quiz_name.QuizName(category='QC', level=1, name='eletricity', quiz_id=quizid)
    dataDir = data_dir.DataDir()
    json_file = os.path.join(dataDir.json_dir, quizName.json)
    # write to file/not sql
    pjson = ParseJson()
    pjson.dict2json(quiz_dict, json_file)
    data_dir = pjson.data_dir
    file_to_write = os.path.join(data_dir, file_to_write)
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
