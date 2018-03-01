import re
import unittest


class TestReFindAll(unittest.TestCase):

    def test_findall_1(self):
        # demo of the usage of re.escape
        s = '111 222 (*+?) 333'
        reg = re.escape(r'(*+?)')
        items = re.findall(reg, s)
        self.assertEqual(items, ['(*+?)'])

    def test_split_1(self):
        s = ' I have a dog   ,   you have a dog  ,  he have a dog '
        items = re.split('\s*,\s*', s)
        self.assertEqual(items, [' I have a dog', 'you have a dog', 'he have a dog '])

    def test_finditer_1(self):
        s = '111 222 333 444'
        items = re.finditer(r'\d+', s)
        groups = []
        spans = []
        for item in items:
            groups.append(item.group())
            spans.append(item.span())

        self.assertEqual(groups, ['111', '222', '333', '444'])
        self.assertEqual(spans, [(0, 3), (4, 7), (8, 11), (12, 15)])

    def test_compile(self):
        """
        compile is used for reusage and efficiency
        """
        s = '111,222,aaa,bbb,ccc333,444ddd'
        reg = r'\b\d+\b'
        compiled_rule = re.compile(reg)
        # could be match/search/findall etc
        items = compiled_rule.findall(s)
        self.assertEqual(items, ['111', '222'])

    def test_split44(self):
        import subprocess
        import os
        dirname = os.path.dirname(__file__)
        cmds = ['cat', "{}/1.txt".format(dirname)]
        txt = subprocess.check_output(cmds)
        items = re.findall(r"[\r\n]+(?!;500)", txt)
        self.assertEqual(items, [])
        for item in items:
            self.assertEqual(item, ' ')
