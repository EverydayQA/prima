
from lib.addquiz import add_quiz
from lib import quiz as qz
from add import add_quiz


result = add_quiz.Quiz().get()
print result

result = qz.Quiz().get()
print result

result = add_quiz.add_test.AddTest().get()
print result
