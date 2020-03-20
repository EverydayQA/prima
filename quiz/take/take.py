#!/usr/bin/python
import logging
import quiz
import glob
import os
import sys
import argparse
from ..lib import menu
from ..lib import parse_json
from ..lib import quiz_name
from ..lib import quiz_content
from ..lib import tools
from ..lib import data_dir
from collections import OrderedDict
import uuid
import mechanize
from time import sleep
import subprocess

class Taken(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @property
    def session_id(self):
        session_id = self.kwargs.get('session_id')
        return session_id

    @property
    def quiz_id(self):
        quiz_id = self.kwargs.get('quiz_id')
        return quiz_id

    @property
    def file_name(self):
        file_name = self.kwargs.get('file_name')
        return file_name

    @property
    def pass_count(self):
        pass

    @property
    def fail_count(self):
        pass

    def __str__(self):
        return 'Taken {0} {1} {2} {3} {4} {5}'.format(self.session_id, self.quizid, self.file_name, self.pass_count, self.fail_count)

    def __repr__(self):
        return '{0}(args: {1} kwargs: {2})' % (self.__class__, self.args, self.kwargs)

    def __dict__(self):
        return
    # file_name/quiz_id/session_id(same)/ans/result/datetime/userid
    # Users() - with login/password/email/phone/
    # Sessions() - session_id/user/datetime/score
    # Taken() quiz_id/session_id/extra - fail_count/pass_count/result/ans
    # Quiz() quiz_id/description/questions/answers/group_id(o)
    # modify/delete/quality request

class Take(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @property
    def logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(10)
        return logger

    @property
    def session_id(self):    
        session_id = self.kwargs.get('session_id', 1000)
        return session_id

    def jsons_glob(self, jason_dir): 
        jsons = glob.iglob(jason_dir + '/*.json')
        return jsons

    def jsons_walk(self, jason_dir):
        jsons = []
        for root, dirs, files in os.walk(jason_dir):
            for file in files:
                if 'to_delete' in root:
                    continue
                if file.endswith('.json'):
                    jsons.append(os.path.join(root, file))
        return jsons

    def sort_quiz_dict_by_desc(self, list_dict):
        print '\n\n*sorted BY DESCRIPTION {0}\n'.format( len(list_dict))    
        sorted_dict_desc = OrderedDict(sorted(list_dict.items(),  key=lambda t: t[1].description) )
        for key in sorted_dict_desc:
            item = sorted_dict_desc[key]
            self.logger.debug( str(key) + "-----" + str(item.description) )

        return sorted_dict_desc

    def sort_quiz_dict_by_key(self, list_dict):

        print '\n\n*sorted BY KEY {0}\n'.format(len(list_dict))    
        list_dict = OrderedDict(sorted(list_dict.items(),  key=lambda t:t[0]) )
        for key in list_dict:
            item = list_dict[key]
            self.logger.debug( str(key) + "-----" + str(item.description) )
        return list_dict

class Score(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    
def init_args_take():
    parser = argparse.ArgumentParser()
    parser.add_argument('--logging', type=int, default=20, help='logging level')
    parser.add_argument('--category', type=str, default='QC', help='Category')
    parser.add_argument('--level', type=int, default=20, help='level in category')
    parser.add_argument('--name', type=str, default='name', help='course name')

    args, args_extra = parser.parse_known_args(sys.argv[1:] )
    return args, args_extra

def main():
    args, args_extra = init_args_take()

    name = os.path.splitext(os.path.basename(__file__))[0]
    logger = logging.getLogger(name)

    logger.setLevel(args.logging)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(args.logging)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.propagate = False 
    dataDir = data_dir.DataDir()

    # now - a comprised way to get quiz.json first
    take = Take()
    jsons = take.jsons_walk(dataDir.json_dir)

    # available Quiz()
    logger.info('find available Quiz()s -- with quiz_id etc')
    
    list_dict = {}
    # choose a List()/Apply same session_id
    pjson = parse_json.ParseJson()
    logger.info('test sorting list of class obj')
    for json in jsons:
        quiz_dict = pjson.read_json(json)
        qz = pjson.dict2quiz(quiz_dict)
        rand_str = str( uuid.uuid4() )
        key = rand_str + "." + json 
        logger.info(key)
        list_dict[key] = qz

    sorted_dict = take.sort_quiz_dict_by_desc(list_dict)
    sorted_dict = take.sort_quiz_dict_by_key(list_dict)


    logger.info('now - take Quiz -- json-Quiz()')

    # select Quiz()
    files = menu.select_from_list(jsons)
    print files

    taken_dict = {}
    # file_name/quiz_id/session_id(same)/ans/result/datetime/userid

    for json in files:
        quiz_dict = pjson.read_json(json)
        logger.info(quiz_dict)

        qz = pjson.dict2quiz(quiz_dict)

        sels = qz.multiple_choices()
        logger.info(sels)

        ans = qz.answers
        logger.info(ans)
        result = qz.quiz_result(sels)
        logger.info(result)

        # a choice to modify(category/level) or delete the question
        tool = tools.Tools()
        prompt = tool.prompt('type r(emove) to delete this question\n')
        if 'r' in prompt:
            cmds = ['mv', json, dataDir.json_dir_to_delete]
            tool.to_system(cmds, True)

    logger.info('later - Taken() - ')
    # write back to AnswerList-- Answer()??? or 

    logger.info('later - Summary() or Score()')

if __name__ == '__main__':
    main()
