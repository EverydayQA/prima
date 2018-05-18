from course import Course


class French(Course):

    @property
    def book(self):
        return 'french literature'

    def get_instructor(self):
        return 'fake'

    def get_student(self, id):
        return id

    @property
    def level(self):
        return 1

    def get_credit(self, course_id):
        return 3

    def get_campus(self, course_id):
        """
        """
        return 'north'

    def get_class_room(self, course_id):
        return '211'

    def add_course(self):
        d = {}
        d['add_course'] = 'french'
        return d
