#!/usr/bin/python
import json
import simplejson
import sys
from pprint import pprint
# args 

class AddQuiz(object):
    def __init__(self, category):
        self.category = category

    def add(self):
        # add question to category
        # data/category
        # multiple choices format using either XML or Jason
        # png/jpg/gif
        return;
    def read_json(self, file_json):
        data_list = []
        with open(file_json, 'r') as f:
            data_list = json.load(f)

        return data_list    

    def write_dict_to_json(self, data_dict, file_json):
        d = {"name":"interpolator", \
             "children":[{'name':key,"size":value} \
             for key,value in data_dict.items()]}

        with open(file_json, 'w') as f:
            j = json.dumps(d, indent=4)
            print >> f, j
            f.close()

if __name__ == '__main__':
    add_quiz = AddQuiz('QC')
    sample_dict = {'aaa':1, 'ccc':3}
    add_quiz.write_dict_to_json(sample_dict, 'menu.json')

    data_list = add_quiz.read_json('menu.json')
    print "\n\n"
    print data_list
    sys.exit()

