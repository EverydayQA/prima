#!/usr/bin/python
import logging
import menu
import quiz
import glob
import os
import sys
import menu
import parse_json
import quiz
from collections import OrderedDict
import uuid
name = os.path.splitext(os.path.basename(__file__))[0]
logger = logging.getLogger(name)

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
    def data_dir(self):    
        dirname = os.path.dirname(__file__)
        data_dir = os.path.join(dirname, '../data')
        return data_dir
    @property
    def session_id(self):    
        session_id = self.kwargs.get('session_id', 1000)
        return session_id

    def jsons_glob(self, data_dir): 
        jsons = glob.iglob(data_dir + '/*.json')
        return jsons

    def jsons_walk(self, data_dir):
        jsons = []
        for root, dirs, files in os.walk(data_dir):
            for file in files:
                if file.endswith('.json'):
                    jsons.append(os.path.join(root, file))
        return jsons
    def sort_quiz_dict_by_desc(self, list_dict):
        print '\n\n*sorted BY DESCRIPTION {0}\n'.format( len(list_dict))    
        sorted_dict_desc = OrderedDict(sorted(list_dict.items(),  key=lambda t: t[1].description) )
        for key in sorted_dict_desc:
            item = sorted_dict_desc[key]
            logger.debug( str(key) + "-----" + str(item.description) )

        return sorted_dict_desc
    def sort_quiz_dict_by_key(self, list_dict):

        print '\n\n*sorted BY KEY {0}\n'.format(len(list_dict))    
        list_dict = OrderedDict(sorted(list_dict.items(),  key=lambda t:t[0]) )
        for key in list_dict:
            item = list_dict[key]
            logger.debug( str(key) + "-----" + str(item.description) )
        return list_dict

class Score(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    

def main():
    logger.setLevel(10)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(10)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.propagate = True  

    # now - a comprised way to get quiz.json first
    take = Take()
    jsons = take.jsons_walk(take.data_dir)

    # available Quiz()
    logger.info('find available Quiz()s -- with quiz_id etc')

    list_dict = {}
    # choose a List()/Apply same session_id
    logger.info('put Quiz()s in Dict')

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


    logger.info('later - Taken() - ')
    # write back to AnswerList-- Answer()??? or 

    logger.info('later - Summary() or Score()')

if __name__ == '__main__':
    main()
