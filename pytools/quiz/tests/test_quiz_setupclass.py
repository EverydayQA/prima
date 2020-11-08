import unittest


def setUpModule():
    pass


def tearDownModule():
    pass


class QuizUnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._testdir = '/tmp/testdir'
        cls._testfile = 'test.json'

    @classmethod
    def tearDownClass(cls):
        cls._testdir = ''
        cls._testfile = ''


class QuizQATest(QuizUnitTest):

    @classmethod
    def setUpClass(cls):
        super(QuizQATest, cls).setUpClass()
        cls._img = 'test.png'

    @classmethod
    def tearDownClass(cls):
        super(QuizQATest, cls).tearDownClass()
        cls._img = ''

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testdir(self):
        self.assertEqual(self._testdir, '/tmp/testdir')

    def test_testfile(self):
        self.assertEqual(self._testfile, 'test.json')

    def test_testimg(self):
        self.assertEqual(self._img, 'test.png')
