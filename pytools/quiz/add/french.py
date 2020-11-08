from quiz.add import add_quiz
from pprint import pprint
from logg import other_logger
logger = other_logger.logger(__name__)


class French(add_quiz.AddQuiz):
    """
    Inherit AddQuiz
    call subjects/french.add_course()
    """

    def check_course(self):
        logger.info('check course')
        from quiz.subjects import french as fre
        fr = fre.French(**self.shared_kwargs)
        d = fr.add_course()
        pprint(d)
        return d
