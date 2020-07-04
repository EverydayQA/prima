import re
import string
import subprocess

class Tools(object):
    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        self.args = args

    def prompt(self, note):
        prompt = raw_input(note)
        return prompt
    
    def to_system(self, cmds, run):
        if not cmds:
            return
        print cmds
        if not run:
            return
        try:
            subprocess.call(cmds)
        except Exception as e:
            pass
