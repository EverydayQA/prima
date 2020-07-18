import argparse
import json
import os
from stock.single_stock import ConstStock


class StockLog(ConstStock):

    def __init__(self, *args, **kwargs):
        # only args input, the rest goes to each func
        self.args = args
        self.kwargs = kwargs
        self.ns = argparse.Namespace(**kwargs)

    def log_append(self, d):
        # log to file
        log = self.get_logfile()
        jsonstr = json.dumps(d)
        # write
        f = open(log, "a+")
        f.write(jsonstr)
        f.write('\n')
        f.close()
        return d

    def get_logpath(self):
        path = os.path.dirname(__file__)
        path = os.path.join(path, "./data")
        return os.path.abspath(path)

    def get_logfile(self):
        path = self.get_logpath()
        return os.path.join(path, 'stock.json')

    def get_all(self):
        """
        get stock from -- logfile(instead of sqldb)
        feel like it should not be here
        """
        # read log
        d = {}
        log = self.get_logfile()
        if not os.path.isfile(log):
            return d
        f = open(log, "r")
        if f.mode == 'r':
            lines = f.readlines()
            for line in lines:
                dline = json.loads(line)
                d.update(dline)
        f.close()
        return d
