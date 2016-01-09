import unittest
class ScriptTest(unittest.TestCase):
    def test_script(self):
        output=runScript('test.py --a 5 --b 3')
        self.assertEqual(output, '8') 
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ScriptTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
