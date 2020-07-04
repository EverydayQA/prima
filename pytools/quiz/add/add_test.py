import add_quiz


class AddTest(object):

    def get(self):
        result = 'hello from addTest'
        res = add_quiz.Quiz().get()
        result = result + res
        return result
