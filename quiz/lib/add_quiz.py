#!/usr/bin/python
import json
import simplejson
import sys
from pprint import pprint
# args 

class AddQuiz(object):
    def __init__(self, category):
        self.category = category

    def add_question(self):
        file_add = file_to_write()    
        sample_dict = {'aaa':1, 'ccc':3}
        
        # add question to data/self.category/file_name.json
        # self.category
        # file_name - to be decided later on by a function
        # multiple choices format using either XML or Jason
        write_dict_to_json(sample_dict, file_add)

        # png/jpg/gif
        return 8;
    def file_to_write(self):
        file_base = '333.json'
        file_new = os.path.join(data_dir, self.category, file_base)
        return file_new

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

def main():    
    # choose category
    categories = ['QC', 'python']
    category = select_from_list(categories, 'Please choose a category')

    add_quiz = AddQuiz(category)
    json2write = add_quiz.file_to_write(category)

    # ways to add
    # from existing files with different format --> converted to json
    # from input -> convert to dict
    # from dict ()
    sample_dict = {'aaa':1, 'ccc':3}

    add_quiz.write_dict_to_json(sample_dict, json2write)

    # read a json file
    data_list = add_quiz.read_json(json2write)
    print data_list

if __name__ == '__main__':
    main()


