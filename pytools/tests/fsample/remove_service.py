#!/usr/bin/python
import os.path
import os


class RemovalService(object):
    ''' removing objects from file systems?'''

    def rm_file(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)
