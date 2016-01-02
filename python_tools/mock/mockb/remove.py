#!/usr/bin/python
import os.path
import os
class RemovalService(object):
    ''' removing objects from file systems?'''
    # self must be added for class
    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)
