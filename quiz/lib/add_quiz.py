#!/usr/bin/python
import json
import simplejson
import sys

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
        with open(file_json, 'r') as f:
            json.load(f)

    def write_dict_to_json(self, data_dict, file_json):
        d = {"name":"interpolator", \
             "children":[{'name':key,"size":value} \
             for key,value in data_dict.items()]}

        with open(file_json, 'w') as f:
            j = json.dumps(d, indent=4)
            print >> f, j
            f.close()


    def put(self, data, filename):
        try:
            jsondata = simplejson.dumps(data, indent=4,skipkeys=True, sort_keys=True)
            fd = open(filename,'w')
            fd.wirte(jsondata)
            fd.close()
        except:
            print "Error writing ", filename

    def get(self, filename):
        returndata = {}
        text = ''
        try:
            fd = open(filename,'r')
            text = fd.read()
            print text
            fd.close()
            # this did not work
            returndata = json.read(text)

        except:
            print "Could not load <" + filename + ">"

if __name__ == '__main__':
    add_quiz = AddQuiz('QC')
    sample_dict = {'aaa':1, 'ccc':3}
    add_quiz.write_dict_to_json(sample_dict, 'menu.json')

    add_quiz.get('menu.json')
    sys.exit()

