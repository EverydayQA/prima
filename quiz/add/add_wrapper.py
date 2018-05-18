# from add_quiz import AddQuiz
from pprint import pprint
from quiz.add import french
"""
import all class names to have variable class name works
"""


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
        cls_name = self.match_d_cli_with_class()
        print cls_name

        klass = getattr(french, cls_name)
        cls_obj = klass(**self.kwargs)
        d = cls_obj.check_course()
        print 'variable cls name with check_course()'
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
