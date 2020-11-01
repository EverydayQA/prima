import os
import datetime
import getpass


class LogName(object):
    """
    proper name for FileHander
    """

    def logbase(self, items):
        """
        without ext
        """
        return '.'.join(items)

    def d_names(self, name=None):
        d = {}
        datestr = datetime.datetime.now().strftime("%Y-%m-%d")
        user = getpass.getuser()
        d['name'] = __name__
        if name:
            d['name'] = name
        d['date'] = datestr
        d['user'] = user
        return d

    def log_basename(self, name=None):
        d = self.d_names(name=name)
        items = d.values()
        filebase = self.logbase(items)
        return '{}.log'.format(filebase)

    def get_log(self, name=None):
        basename = self.log_basename(name=name)
        return os.path.join(self.other_logdir(), basename)

    def get_errlog(self, name=None):
        log = self.get_log(name=name)
        log = log.replace('.log', '.errlog')
        return log

    def other_logdir(self):
        """
        if not specified?
        """
        return '/tmp'

    def logdir(self):
        """
        a default test log directory
        """
        return '/tmp/var/log'

    def check_logfile(self, log):
        """
        messy
        what if a logfile is provided?
        """
        if not log:
            return self.logfile_tmp()
        if '/' not in log:
            return os.path.join('/tmp', log)
        dirname = os.path.dirname(os.path.abspath(log))
        if not os.path.isdir(dirname):
            return os.path.join('/tmp', log)
        return log
