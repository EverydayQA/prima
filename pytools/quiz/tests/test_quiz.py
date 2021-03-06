import unittest
import sys
import argparse


class QuizTest(unittest.TestCase):

    def __init__(self, methodName='runTest', args=None):
        super(QuizTest, self).__init__(methodName)
        self.args = args


class QuizQATest(QuizTest):

    def test_if_verbose(self):
        if not self.args:
            self.assertEqual(self.args, None)
            return
        if self.args.verbose:
            self.assertTrue(self.args.verbose, True)
        else:
            self.assertFalse(self.args.verbose)


class QuizPythonTest(QuizTest):

    def test_pass_anything(self):
        if not self.args:
            self.assertEqual(self.args, None)
            return

        self.assertTrue(self.args.verbose)


def make_suite(testcase_class, args):
    testloader = unittest.TestLoader()
    testnames = testloader.getTestCaseNames(testcase_class)
    suite = unittest.TestSuite()
    for name in testnames:
        suite.addTest(testcase_class(name, args=args))
    return suite


def init_args_unittest():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-?", '--help', action="help", help='xxx')
    parser.add_argument("-v", '--verbose', action='store_true', dest='verbose', help='verbose')
    parser.add_argument('files', nargs='*')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = init_args_unittest()
    test_suite = unittest.TestSuite()
    test_suite.addTest(make_suite(QuizTest, args))
    test_suite.addTest(make_suite(QuizQATest, args))
    test_suite.addTest(make_suite(QuizPythonTest, args))
    result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    sys.exit(not result.wasSuccessful())
