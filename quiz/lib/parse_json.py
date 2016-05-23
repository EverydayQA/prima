#!/usr/bin/python
import json
import sys
import os
import logging
pwd = os.path.dirname(os.path.realpath(__file__))
base_dir = os.path.join(pwd,'../data/')
base_dir  = os.path.abspath(base_dir)
employee_json = os.path.join(base_dir, 'qz_111.json')
import quiz
# Jason -> dict -->  Quiz 
class ParseJson(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        name = __name__ + '.' + self.__class__.__name__
        self.logger = logging.getLogger(name)

    # return an instance of Quiz()
    def read_json(self, file_json):
        data_list = []
        quiz_dict = {}
        with open(file_json, 'r') as f:
            data_list = json.load(f)
            for key, value in data_list.iteritems():
                if type(value) is unicode:
                    quiz_dict[key] = value
                elif type(value) is list:
                    quiz_dict[key] = value
                    for item in value:
                        if type(item) is dict:
                            for x, y in item.iteritems():
                                pass
                        
        return quiz_dict    

    def json2dict(self, file_json):
        quiz_dict = {}
        with open(file_json, 'r') as f:
            data_list = json.load(f)
            for key, value in data_list.iteritems():
                quiz_dict[key] = value
        return quiz_dict   
    def dict2quiz(self, quiz_dict):
        qz = quiz.Quiz(description=quiz_dict.get('description'), questions=quiz_dict.get('questions'))
        return qz

    # dict
    def write_dict_to_json(self, data_dict, file_json):
        d = {"name":"interpolator", \
             "children":[{'name':key,"size":value} \
             for key,value in data_dict.items()]}

        with open(file_json, 'w') as f:
            j = json.dumps(d, indent=4, sort_keys=True)
            print >> f, j
            f.close()
def main():
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=FORMAT)
    logger = logging.getLogger(__name__)
    logger.propagate = True  
    logger.setLevel(10)
    el  = logger.getEffectiveLevel()
    line = 'logger level is: {0} args logging {1} EffectiveLevel {2}\n'.format(logger.level, 10, el)

    ch = logging.StreamHandler(sys.stdout)
    #ch.setLevel(10)
    logger.addHandler(ch)

    logger.debug(line)

    logger.info(__name__)
    pjson = ParseJson('QC')
    sample_dict = {'aaa':1, 'ccc':3}
    pjson.write_dict_to_json(sample_dict, 'menu.json')

    quiz_dict = pjson.read_json('menu.json')
    logger.info(quiz_dict)

    logger.info(employee_json)
    quiz_dict = pjson.json2dict(employee_json)
    logger.info( quiz_dict )
    qz = pjson.dict2quiz(quiz_dict)
    sels = qz.multiple_choices()
    logger.info(sels)
    result = qz.quiz_result(sels)
    logger.info(result)

    # add result to dict quizID 
    quiz_alist = {}
    quizid = qz.quizid
    quiz_alist[quizid] = result
    logger.info(quiz_alist)

if __name__ == '__main__':
    main()

