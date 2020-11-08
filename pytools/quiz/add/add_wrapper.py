# from add_quiz import AddQuiz
from pprint import pprint
from logg import other_logger
logger = other_logger.logger(__name__)


class AddWrapper(object):
    """
    will have to import all quiz/add/modules?!
    """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def dispatch(self):
        """
        get kwargs from AddQuiz()
        assign variable class name with kwargs
        call add_course in variable class
        and action based on d returned from call()
        # pass namespace as kwargs to AddQuiz()
        addquiz = AddQuiz(self.args, **self.kwargs)
        pprint(addquiz.shared_kwargs)
        """
        logger.debug(self.__module__.__class__.__name__)
        cls_name = self.match_d_cli_with_class()

        from quiz.add import french
        klass = getattr(french, cls_name)
        cls_obj = klass(**self.kwargs)
        d = cls_obj.check_course()
        logger.debug('variable class name')
        pprint(d)

        # to do
        #
        # from quiz.subjects import french
        # find variable clsname from add/ dealing from there
        # pass to each class in add/french to make warpper simple
        # one import per course

    def match_d_cli_with_class(self):
        """
        match class name based on cli args
        """
        return 'French'
