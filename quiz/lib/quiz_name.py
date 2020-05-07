import json
import simplejson
import sys
import os
from pprint import pprint
import logging
from . import menu
import inspect
import argparse
import operator
logger = logging.getLogger(__name__)


class QuizName(object):
    def __init__(self, *args, **kwargs):
        name = os.path.splitext(os.path.basename(__file__))[0] + "." + self.__class__.__name__
        logger.propagate = True    
        el  = logger.getEffectiveLevel()
        self.args = args
        self.kwargs = kwargs
    
    def __repr__(self):
        return 'QuizName({0}, {1}, {2}, {3})'.format(self.category, self.level, self.name, self.quizquiz_id)

    def __str__(self):
        return 'An instance of QuizName(category: {0}, level: {1}, name: {2}, quiz_id: {3})'.format(self.category, self.level, self.name, self.quizquiz_id)

    @property
    def category(self):
        category = self.kwargs.get('category', 'QC')
        return category

    @property
    def level(self):
        level = self.kwargs.get('level', 0)
        return level

    @property
    def name(self):
        name = self.kwargs.get('name', None)
        return name

    @property
    def quiz_id(self):
        id = self.kwargs.get('quiz_id', 0)
        return id

    @property
    def json(self):
        names = [self.category, str(self.level), self.name, str(self.quiz_id)]
        names = filter(None, names)
        file_root = '_'.join(names)
        json = file_root + '.json'
        return json
