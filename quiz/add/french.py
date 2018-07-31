import add_quiz
from pprint import pprint
from quiz.subjects import french as fre


class French(add_quiz.AddQuiz):
    """
    Inherit AddQuiz
    call subjects/french.add_course()
    """

    def check_course(self):
        print('\n\n*** quiz.add.french.French.check_course')
        fr = fre.French(**self.shared_kwargs)
        d = fr.add_course()
        pprint(d)
        print('\n\n*** quiz.add.french.French.check_course')

        return d
