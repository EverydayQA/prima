#!/usr/bnin/python
import unittest
import os
import subprocess

import logging

class TestEnv(unittest.TestCase):
    def test_env(self):
        d = dict(os.environ)
        d['TEST_VAR'] = str(1234)
        cmds = ['env']
        exit_code = subprocess.Popen(cmds, shell=True, env=d).wait()
        line = 'exit_code {0}'.format(exit_code)
        print line


        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEnv)
    unittest.TextTestRunner(verbosity=2).run(suite)

