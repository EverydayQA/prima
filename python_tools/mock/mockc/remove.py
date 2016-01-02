#!/usr/bin/python
import os.path
import os
class RemovalService(object):
    ''' removing objects from file systems?'''
    # self must be added for class
    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)
class UploadService(object):
    def __init__(self, removal_service):
        self.removal_service = removal_service
    
    def upload_complete(self, filename):
        self.removal_service.rm(filename)




