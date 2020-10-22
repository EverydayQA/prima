import os
from termcolor import cprint
from datetime import datetime


class FileDatetime(object):

    def create_time(self, file):
        """
        datetime obj?
        """
        created = os.path.getctime(file)
        dt = datetime.fromtimestamp(created)
        stat = os.stat(file)
        print(stat)
        dtm = self.modified_time(file)
        if dt < dtm:
            cprint('create time {}'.format(dt), 'green')
            return dt
        cprint('create time {}'.format(dtm), 'green')
        return dtm

    def modified_time(self, file):
        modified = os.path.getmtime(file)
        dt = datetime.fromtimestamp(modified)
        # return os.stat(file)[-2]
        # return os.stat(file).st_mtime
        return dt

    def date_string_ctime_file(self, file):
        dt = self.create_time(file)
        return self.date_string(dt)

    def datetime_string_ctime_file(self, file):
        dt = self.create_time(file)
        return self.datetime_string(dt)

    def date_string(self, dt):
        """
        for subdir
        """
        return dt.strftime("%Y-%m-%d")

    def datetime_string(self, dt):
        """
        for filename
        """
        return dt.strftime("%Y-%m-%d_%H-%M-%S")

    def exif_datetime_str_to_datetime(self, datestr):
        """
        assume this format 2016:07:28 16:13:57
        """
        return datetime.strptime(datestr, '%Y:%m:%d %H:%M:%S')
