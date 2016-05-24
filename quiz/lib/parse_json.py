#!/usr/bin/python
import json
import sys
import os
import logging
pwd = os.path.dirname(os.path.realpath(__file__))
base_dir = os.path.join(pwd,'../data/')
base_dir  = os.path.abspath(base_dir)
quiz_111_json = os.path.join(base_dir, 'qz_111.json')
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
        qz = quiz.Quiz(quizid=quiz_dict.get('quizid'), description=quiz_dict.get('description'), questions=quiz_dict.get('questions'), answers=quiz_dict.get('answers'), category=quiz_dict.get('category'), weight=quiz_dict.get('weight'))
        return qz

    # dict2json
    def dict2json(self, data_dict, file_json):
        with open(file_json, 'w') as f:
            j = json.dumps(data_dict, indent=4, sort_keys=True)
            print >> f, j
            f.close()
    @property
    def data_dir(self):
        return base_dir
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
    pjson = ParseJson()



    logger.info(quiz_111_json)
    quiz_dict = pjson.json2dict(quiz_111_json)
    logger.info( quiz_dict )

    qz = pjson.dict2quiz(quiz_dict)
    sels = qz.multiple_choices()
    logger.info(sels)

    ans = qz.answers
    logger.info(ans)

    result = qz.quiz_result(sels)
    logger.info(result)

    # add result to dict quizID 
    quiz_alist = {}
    quizid = qz.quizid
    logger.info(quizid)
    quiz_alist[quizid] = result
    logger.info(quiz_alist)

    # dict2json
    file_to_write  = os.path.join("/tmp", 'menu.json')
    pjson.dict2json(quiz_dict, file_to_write)
    quiz_dict = pjson.read_json(file_to_write)
    logger.info(quiz_dict)

if __name__ == '__main__':
    main()

