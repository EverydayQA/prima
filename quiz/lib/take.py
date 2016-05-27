#!/usr/bin/python
import logging
import menu
import quiz
import glob
import os
import sys

logger = logging.getLogger(__name__)

class Taken(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @property
    def sessionid(self):
        
        sessionid = self.kwargs.get('sessionid')
        return sessionid
    @property
    def quizid(self):
        quizid = self.kwargs.get('quizid')
        return quizid

    @property
    def pass_count(self):
        pass

    @property
    def fail_count(self):
        pass

    # extra for Quiz() userid/time/sessionid/score/

    #Quiz() group - pass(no need to do this cat) fail(more on this group)
    # modify/delete/quality request

class Take(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

class Score(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    

def main():

    # now - a comprised way to get quiz.json first
    dirname = os.path.dirname(__file__)
    data_dir = os.path.join(dirname, '../data')
    jsons = glob.iglob(data_dir + '/*.json')
    logger.info(jsons)
    
    jsons = []
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.json'):
                jsons.append(os.path.join(root, file))


    # available Quiz()
    logger.info('find available Quiz()s -- with quiz_id etc')

    # choose a List()/Apply same session_id
    logger.info('put Quiz()s in Dict')

    # select Quiz()
    json = menu.select_from_list(jsons)
    print json


    logger.info('now - take Quiz -- json-Quiz()')

    logger.info('later - Taken() - ')
    # write back to AnswerList-- Answer()??? or 

    logger.info('later - Summary() or Score()')

if __name__ == '__main__':
    main()
