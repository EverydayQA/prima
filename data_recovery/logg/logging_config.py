import os
import datetime
import getpass
import logging


class LoggingConfig(object):

    """
    LOGGING-LEVEL in env for both logfile and console
    each module could has the same logfile and logging-level of their own
    but env logging-level is for every module of the session
    """

    LOGGING_LEVEL_CONSOLE = 'LOGGING_LEVEL_CONSOLE'
    LOGGING_FILE = 'LOGGING_FILE'
    ERROR_LOGGING_FILE = 'ERROR_LOGGING_FILE'
    LOGGING_LEVEL_FILE = 'LOGGING_LEVEL_FILE'

    LOGFORMAT = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
    # LOGFORMAT = "%(log_color)s - %(asctime)s - %(name)-12s - %(levelname)s - %(message)s",

    # for CONSOLE_LOGGING
    CFORMAT_LONG = "%(log_color)s[%(asctime)s %(levelname)-8s%(module)s]%(reset)s %(white)s%(message)s"

    def keys_envconfig(self):
        return [self.LOGGING_FILE, self.ERROR_LOGGING_FILE, self.LOGGING_LEVEL_CONSOLE, self.LOGGING_LEVEL_FILE]

    def get_envconfig(self):
        d = {}
        for key in self.keys_envconfig():
            d[key] = os.environ.get(key, None)
        return d

    @property
    def format_simple(self):
        # return self.LOGFORMAT
        return '%(name)-12s: %(levelname)-8s %(message)s'

    @property
    def format_verbose(self):
        return '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'

    def getenv_logging_level(self, field):
        """
        int
        """
        level = os.environ.get(field)
        if level:
            return level
        return logging.INFO

    def setenv_logging_level(self, field, level):
        """
        input: type int
        :rtype: int(str)
        """
        if not isinstance(level, int):
            print(level)
            raise Exception('set logging level must be int')
        os.environ[field] = str(level)
        return int(level)

    def get_logfile_basename(self):
        datestr = datetime.datetime.now().strftime("%Y-%m-%d")
        user = getpass.getuser()
        filename = '{}.{}.{}.log'.format(__name__, datestr, user)
        return filename

    def logfile_tmp(self):
        dirname = '/tmp'
        filename = self.get_logfile_basename()
        return os.path.join(dirname, filename)

    def check_logfile(self, log):
        if not log:
            return self.logfile_tmp()
        if '/' not in log:
            return os.path.join('/tmp', log)
        dirname = os.path.dirname(os.path.abspath(log))
        if not os.path.isdir(dirname):
            return os.path.join('/tmp', log)
        return log

    def setenv_errlog(self, log):
        """
        check before set
        """
        log = self.check_logfile(log)
        log = '{}.errlog'.format(log)
        os.environ[self.ERROR_LOGGING_FILE] = log
        return log

    def setenv_logfile(self, log):
        """
        check before set
        """
        log = self.check_logfile(log)
        os.environ[self.LOGGING_FILE] = log
        return log
