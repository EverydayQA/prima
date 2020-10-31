import os
import logging


class LoggingCommon(object):

    """
    LOGGING-LEVEL in env for both logfile and console
    each module could has the same logfile and logging-level of their own
    but env logging-level is for every module of the session
    """

    LOGGING_LEVEL_FILE = 'LOGGING_LEVEL_FILE'
    LOGGING_LEVEL_CONSOLE = 'LOGGING_LEVEL_CONSOLE'
    LOGGING_FILE = 'LOGGING_FILE'
    LOGFORMAT = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
    # LOGFORMAT = "%(log_color)s - %(asctime)s - %(name)-12s - %(levelname)s - %(message)s",

    # for CONSOLE_LOGGING
    CFORMAT_LONG = "%(log_color)s[%(asctime)s %(levelname)-8s%(module)s]%(reset)s %(white)s%(message)s"

    @property
    def format_simple(self):
        # return self.LOGFORMAT
        return '%(name)-12s: %(levelname)-8s %(message)s'

    @property
    def format_verbose(self):
        return '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'

    def get_name(self):
        return self.__module__

    def names(self):
        """
        experimental
        """
        d = {}
        d['__name__'] = __name__

        d['__module__'] = self.__module__

        d['mixed'] = '{}.{}'.format(self.__module__, self.__class__.__name__)
        return d

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
