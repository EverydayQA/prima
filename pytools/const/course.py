ENGLISH = 'English'
FRENCH = 'French'
AI = 'Pytorch'
STATISTICS = 'Stat'


class ConstCourse(object):
    """
    alternative usage of constant in class
    """

    @property
    def course_name(self):
        return 'Course'

    @property
    def eng(self):
        return ENGLISH

    @property
    def course_code(self):
        return 'ENG'

    @property
    def stats(self):
        return STATISTICS

    @property
    def ai(self):
        return AI

    @property
    def french(self):
        return FRENCH
