#!/usr/bin/python
import os
import sys
import argparse
from quiz.lib import quiz_name

import add_quiz
from quiz.lib.parse_json import ParseJson


def init_args_addquiz():
    parser = argparse.ArgumentParser()
    parser.add_argument('--logging', type=int, default=20, help='logging level')
    parser.add_argument('--category', type=str, default='QC', help='Category')

    args, args_extra = parser.parse_known_args(sys.argv[1:])
    return args, args_extra


def main():
    args, args_extra = init_args_addquiz()

    # extra args as args, while args serves as kwargs for class AddQuiz
    addquiz = add_quiz.AddQuiz(args_extra, **vars(args))
    quiz_dict = addquiz.set_quiz_dict()

    quizid = addquiz.quizid

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
    qz.answers
    qz.quiz_result(sels)


if __name__ == '__main__':
    main()
