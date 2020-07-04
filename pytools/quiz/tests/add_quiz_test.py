#!/usr/bin/python
import unittest
import os
import sys
from quiz.add import add_quiz

class add_quizTest(unittest.TestCase):
    def test1(self):
        add = add_quiz.AddQuiz(category='QA')
        question = add.set_category()
        self.assertEqual(question,'QA')

    def test2(self):
        add = add_quiz.AddQuiz(category='QC')
        question = add.set_category()
        self.assertEqual(question,'QC')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(add_quizTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
