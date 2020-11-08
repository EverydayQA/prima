import unittest
import os
import subprocess
import re


class TestEnv(unittest.TestCase):

    def test_cmds(self):
        afile = __file__
        dirname = os.path.dirname(afile)
        cmd = os.path.join(dirname, 'test.pl')
        cmds = [cmd, re.escape('TEST VAR'),  'EXIT CODE', 'DEBUG']
        cmds = filter(None, cmds)
        cmds_new = []
        for cmd in cmds:
            cmds_new.append(cmd)

        exit_code = subprocess.call(cmds_new)
        line = 'exit_code {0}'.format(exit_code)
        self.assertEqual(exit_code, 1, line)

    def test_env(self):
        d = dict(os.environ)
        d['TEST_VAR'] = str(1234)
        cmds = ['env']
        exit_code = subprocess.Popen(cmds, shell=False, env=d).wait()
        line = 'exit_code {0}'.format(exit_code)
        self.assertEqual(exit_code, 1, line)
