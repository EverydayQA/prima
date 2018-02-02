# person.py
# change from
#from data_source import get_name
# to this 
import data_source

class Person(object):
    def name(self):
        #return get_name()
        # change - will mock Person not data_source
        return data_source.get_name()

