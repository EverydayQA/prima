import unittest
from quiz.add import add_quiz


class TestAddQuiz(unittest.TestCase):

    def test_set_category(self):
        add = add_quiz.AddQuiz(category='QA')
        question = add.set_category()
        self.assertEqual(question, 'QA')

    def test_aset_category2(self):
        add = add_quiz.AddQuiz(category='QC')
        question = add.set_category()
        self.assertEqual(question, 'QC')
