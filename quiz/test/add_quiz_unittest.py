#!/usr/bin/python
import unittest
import os
import sys
# similar to findBin in Perl
pwd = os.path.dirname(os.path.realpath(__file__))
# 1 level up
base_dir = os.path.join(pwd,'..')
# add to sys.path
sys.path.append(base_dir)

from quiz import add_quiz

class add_quizTest(unittest.TestCase):
    def test1(self):
        question = add_quiz.add_question()
        self.assertEqual(question,4)

    def test2(self):
        question = add_quiz.add_question()
        self.assertEqual(question,8)


if __name__ == '__main__':
    unittest.main()


