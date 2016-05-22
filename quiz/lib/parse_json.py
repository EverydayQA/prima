#!/usr/bin/python
import json
import simplejson
import sys

# Jason -> dict -->  Quiz 
class ParseJson(object):
    def __init__(self, category):
        self.category = category

    def add(self):
        # add question to category
        # data/category
        # multiple choices format using either XML or Jason
        # png/jpg/gif
        return;

    # recursive?
    def read_json(self, file_json):
        data_list = []
        with open(file_json, 'r') as f:
            data_list = json.load(f)
            for key, value in data_list.iteritems():
                print key, value
                if type(value) is unicode:
                    print value
                elif type(value) is list:
                    for item in value:
                        print item, type(item)
                        if type(item) is dict:
                            for x, y in item.iteritems():
                                print x, y
                        
        return data_list    

    # dict
    def write_dict_to_json(self, data_dict, file_json):
        d = {"name":"interpolator", \
             "children":[{'name':key,"size":value} \
             for key,value in data_dict.items()]}

        with open(file_json, 'w') as f:
            j = json.dumps(d, indent=4, sort_keys=True)
            print >> f, j
            f.close()

if __name__ == '__main__':
    parse_json = ParseJson('QC')
    sample_dict = {'aaa':1, 'ccc':3}
    parse_json.write_dict_to_json(sample_dict, 'menu.json')

    data_list = parse_json.read_json('menu.json')
    print "\n\n"
    print data_list
    sys.exit()

