#!/usr/bnin/python
import unittest
import os
import subprocess
import re
import logging

class TestEnv(unittest.TestCase):
    def test_cmds(self):
        cmds = ['./tests/test.pl', re.escape('TEST VAR'),  'EXIT CODE', 'DEBUG']
        cmds = filter(None, cmds)
        cmds_new = []
        for cmd in cmds:
            cmds_new.append(cmd)

        exit_code = subprocess.call(cmds_new)
        line = 'exit_code {0}'.format(exit_code)
        print line
    def test_env(self):
        d = dict(os.environ)
        d['TEST_VAR'] = str(1234)
        cmds = ['env']
        exit_code = subprocess.Popen(cmds, shell=False, env=d).wait()
        line = 'exit_code {0}'.format(exit_code)
        print line

    def test_check_out(self):
        cmds = ['./tests/test.pl', re.escape('TEST VAR'),  'EXIT CODE', 'DEBUG']
        cmds = filter(None, cmds)
        cmds_new = []
        for cmd in cmds:
            cmds_new.append(cmd)

        exit_code = subprocess.call(cmds_new)
        line = 'exit_code {0}'.format(exit_code)
        print line

        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEnv)
    unittest.TextTestRunner(verbosity=2).run(suite)

