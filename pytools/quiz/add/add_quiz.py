#!/usr/bin/python
import os
import logging
from random import randint
from quiz.lib import parse_json


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
        el = logger.getEffectiveLevel()
        line = 'logger level is: {0} args cls {1} EffectiveLevel {2}\n'.format(logger.level, name, el)
        logger.debug(line)
        p = parse_json.ParseJson()
        p.dict2json({})
        return logger 

    def set_category(self):
        self.category = self.kwargs.get('category')
        if not self.category:
            self.category = self.prompt('Please add or select a category: ')
            self.logger.info('prompt_category')
        return self.category

    def set_description(self):
        desc = self.prompt('\n*** Enter the full the question content\n')
        return desc

    def set_quality(self):
        return 50

    def set_weight(self):
        return 1

    def set_quizid(self):
        if self.quizid:
            pass
        else:
            int_random = randint(111, 999)
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
            que = self.prompt('add a few questions(max of 4), q to quit')
            if 'q' in que:
                return questions
            questions.append(que)
        return questions

    def prompt(self, str):
        input_str = None
        while not input_str:
            print(str)
            input_str = raw_input()
        return input_str

    @property
    def shared_kwargs(self):
        return self.update_dict()

    def update_dict(self):
        d = {}
        d['d_cli'] = self.kwargs
        d['ali'] = 1
        d['foo'] = '--foo'
        d['boo'] = '--boo'
        return d

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
