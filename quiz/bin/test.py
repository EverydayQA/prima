from blessings import Terminal
import time

from quiz_lib.addquiz import add_quiz
from quiz_lib import quiz as qz
from quiz_lib import addquiz


result = add_quiz.Quiz().get()
print result

result = qz.Quiz().get()
print result

result = addquiz.add_test.AddTest().get()
print result
