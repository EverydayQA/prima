import unittest


class all_object_runner():

    def __init__(self):

        self.lift=0


class TestGlobal(unittest.TestCase):
    __test__ = False

    @classmethod
    def setUpClass(cls):
        cls.aor = all_object_runner()

    def test_lift_globaly(self):
        self.assertTrue(self.aor.lift >= 0)


class Test_loacl(TestGlobal):

    __test__ = True

    def test_if_lift_localy(self):
        corr=self.aor.lift
        self.assertTrue(corr>=0)


if __name__ == "__main__":
    unittest.main()
