# person.py
# change from
#from data_source import get_name
# to this 
import data_source

class Person(object):
    def __init__(self):
        self.pet = Pet()

    def name(self):
        #return get_name()
        # change - will mock Person not data_source
        return data_source.get_name()

class Pet(object):
    def noise(self):
        return "Woof"

