#!/usr/bin/python
import json
import simplejson

class AddQuiz(object):
    def __init__(self, category, txt_file, json_file):
        self.category = category
        self.txt_file = txt_file
        slef.json_file = json_file

    def add(self):
        # add question to category
        # data/category
        # multiple choices format using either XML or Jason
        # png/jpg/gif
        return;
    def write_json(self):
        with open(self.json_file, 'r') as f:
            data = json.load(f)

    def read_json(self):
        with opn(self.json_file, 'w') as f:
            json.dump(data, f)

    def put(self):
        try:
            jsondata = simplejson.dumps(self.data, indent=4,skipkeys=True, sort_keys=True)
            fd = open(filename,'w')
            fd.wirte(jsondata)
            fd.close()
        except:
            print "Error writing ", filename

    def get(self):
        returndata = {}
        try:
            fd = open(filename,'r')
            text = fd.read()
            fd.close()
            returndata = json.read(txt)
        except:
            print "Could not load " + filename
if __name__ == '__main__':
    add_quiz = AddQuiz('QC')
    o = get(sys.argv[1])
    if o:
        add_quiz.put(o, sys.argv[1])
