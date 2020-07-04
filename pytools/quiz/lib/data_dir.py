import json
import simplejson
import sys
import os
from pprint import pprint
import logging
from . import menu
import inspect
import argparse
import operator
logger = logging.getLogger(__name__)


class DataDir(object):
    def __init__(self, *args, **kwargs):
        name = os.path.splitext(os.path.basename(__file__))[0] + "." + self.__class__.__name__
        logger.propagate = True    
        el  = logger.getEffectiveLevel()
        self.args = args
        self.kwargs = kwargs
    
    def __repr__(self):
        return 'DataDir({0}, {1})'.format(self.jason_dir, self.jason_dir_to_delete)

    def __str__(self):
        return 'An instance of DataDir(json_dir: {0}, json_dir_to_delete: {1})'.format(self.json_dir, json_dir_to_delete)
    
    @property
    def json_dir(self):
        dirname = os.path.dirname(__file__)
        json_dir = os.path.join(dirname, '../data')
        return json_dir

    @property
    def json_dir_to_delete(self):
        return os.path.join(self.json_dir, 'to_delete')

