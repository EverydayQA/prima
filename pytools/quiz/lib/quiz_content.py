import os
import logging
from myutils import menu
import inspect
import argparse
import operator
# from . import quiz_name
logger = logging.getLogger(__name__)


class QuizContent(object):
    # Quiz base class/subclass
    # add *args, **kwargs - all unittest for common usae
    # logger propagate example
    pass


class Quiz(object):

    def __init__(self, *args, **kwargs):
        name = os.path.splitext(os.path.basename(__file__))[0] + "." + self.__class__.__name__
        logger.propagate = True
        el = logger.getEffectiveLevel()
        # this is necessary to pass logger handler to subclass?
        logger.propagate = True
        el = logger.getEffectiveLevel()
        line = 'logger level is: {0} args cls {1} EffectiveLevel {2}\n'.format(logger.level, name, el)
        logger.debug(line)
        self.args = args
        self.kwargs = kwargs

    @property
    def description(self):
        description = self.kwargs.get('description')
        return description

    @property
    def questions(self):
        questions = self.kwargs.get('questions')
        return questions

    @property
    def answers(self):
        answers = self.kwargs.get('answers')
        answers = filter(operator.isNumberType, answers)
        answers = map(int, answers)

    def get(self):
        import add_quiz
        result = add_quiz.Quiz().get()
        result = 'from quiz.Quiz {0}'.format(result)
        return result

    def print_args(self):
        logger.info(self.args)
        logger.info(self.kwargs)

    @property
    def quizid(self):
        qid = self.kwargs.get('quizid')
        return qid

    @property
    def vote(self):
        vote = self.kwargs.get('vote', 0)
        return vote

    @property
    def weight(self):
        weight = self.kwargs.get('weight', 1)
        return weight

    def multiple_choices(self):
        sels = menu.Menu().select_from_menu(self.kwargs.get('questions'), "Select the one(s) you think is correct")
        return sels

    def quiz_result(self, sels):
        result = False
        if sels == self.answers:
            print("u r right")
            result = True
        else:
            print('ur answers is not right')
            result = False
        return result


class QuizQA(Quiz):

    def __init__(self, *args, **kwargs):
        self.category = kwargs.get('category', 'QA')
        super(QuizQA, self).__init__(args, kwargs)
        name = os.path.splitext(os.path.basename(__file__))[0] + "." + self.__class__.__name__

        logger.info('logger alreay defined in base class {0}'.format(name))
        # logger = logging.getLogger(name)
        el = logger.getEffectiveLevel()
        line = 'logger level is: {0} args cls {1} EffectiveLevel {2}\n'.format(logger.level, name, el)
        logger.debug(line)
        self.args = args
        self.kwargs = kwargs

    def print_args(self, x):
        super(QuizQA, self).print_args()
        print(x)
        logger.debug(x)


def init_args():
    # argument may vary
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-?", '--help', action="help", help='xxx')
    parser.add_argument("-category", '--category', type=str, default=None, dest='category', help='category')
    parser.add_argument("-id", '--id', type=str, default=None, dest='id', help='id')
    parser.add_argument("-weight", '--weight', type=float, default=1, dest='weight', help='weight from 0 to 1')

    parser.add_argument("-run", '--run', action='store_true', dest='run', help='run')
    parser.add_argument("-logging", '--logging', type=int, default=30, dest='logging', help='logging level 0 10 20')
    parser.add_argument('-files', "--files", nargs='*')
    parser.add_argument("-description", '--description', type=str, default='descp', dest='description', help='quiz description')
    parser.add_argument("-questions", '--questions', nargs='*',  dest='questions', help='quiz questions')
    parser.add_argument("-answers", '--answers', nargs='*', dest='answers', help='quiz answers')

    args, args_extra = parser.parse_known_args()
    return args, args_extra


def get_full_class_name(cls):
    return cls.__module__ + "." + cls.__class__.__name__


def get_full_func_name():
    func_name = get_full_func_name.__name__
    func_name = inspect.stack()[0][3]
    return func_name


def main():
    args, args_extra = init_args()
    qz = Quiz(*args_extra, **vars(args))
    sels = qz.multiple_choices()
    qz.quiz_result(sels)
