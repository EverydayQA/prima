#!/usr/bin/python
import os.path
import os
import glob


class RemovalService(object):
    ''' removing objects from file systems?'''
    # self must be added for class

    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)

    def glob_files(self, adir, keyword):
        return glob.glob('{}/*{}*'.format(adir, keyword))


class UploadService(object):

    def __init__(self, removal_service):
        self.removal_service = removal_service

    def upload_complete(self, filename):
        self.removal_service.rm(filename)
