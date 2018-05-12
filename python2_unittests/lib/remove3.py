#!/usr/bin/python
import os.path
import os
import glob
DO_IMPORT = False


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

    def glob_files_basename(self, adir, keyword):
        files = self.removal_service.glob_files(adir, keyword)
        items = []
        for afile in files:
            items.append(os.path.basename(afile))
        return items
