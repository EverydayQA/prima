import logging
import os
from logg.logging_config import LoggingConfig
from logging.handlers import RotatingFileHandler
from logging import FileHandler
from logg.log_name import LogName


class MyFileHandler(LoggingConfig):

    def __init__(self):
        self.lname = LogName()

    def get_logger(self, handler):
        """
        more like add handler
        """
        logger = logging.getLogger(__name__)
        for hl in logger.handlers:
            if isinstance(hl, RotatingFileHandler):
                logger.removeHandler(hl)
        # has to be lowest DEBUG in logger, handler level to be effective
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        return logger

    def error_handler(self, name=None):
        """
        dictconfig is not recommended, it has its own syntax
        """
        errlog = os.environ.get(self.ERROR_LOGGING_FILE, None)
        if not errlog:
            return None
        handler = FileHandler(errlog)
        formatter = logging.Formatter(self.format_verbose)
        handler.setFormatter(formatter)
        # always ERROR level
        handler.setLevel(logging.ERROR)
        return handler

    def file_handler(self, name=None, level=None):
        """
        dictconfig is not recommended, it has its own syntax
        """
        log = os.environ.get(self.LOGGING_FILE, None)
        if not log:
            return None
        handler = RotatingFileHandler(log, maxBytes=0, backupCount=10)
        formatter = logging.Formatter(self.format_verbose)
        handler.setFormatter(formatter)
        level = self.logging_level_handler(level=level)
        handler.setLevel(level)
        return handler

    def logging_level_handler(self, level=None):
        """
        keep level=None for the purpose to use different level at certain modules to debug
        logger.getEffectiveLevel()?
        level first if defined
        use env level second
        """
        if level and isinstance(level, int):
            return level

        # default LEVEL, not too much info
        level_env = os.environ.get(self.LOGGING_LEVEL_FILE)
        # environ level is string
        if level_env:
            return int(level_env)
        return logging.WARN

    def setenv(self, level=logging.INFO, name=None):
        """
        Default level -- logging.INFO
        for handler
        input: type int
        :rtype: int
        """
        # log
        os.environ[self.LOGGING_LEVEL_FILE] = str(level)
        os.environ[self.LOGGING_FILE] = self.lname.get_log(name=name)

        # errlog, level is always logging.ERROR
        os.environ[self.ERROR_LOGGING_FILE] = self.lname.get_errlog(name=name)


def main():
    """
    """
    ch = MyFileHandler()
    # set logging-level once at env
    ch.setenv(level=logging.DEBUG, log=None)

    # others
    chander = ch.file_handler(level=None)
    logger = ch.get_logger(chander)

    d = ch.get_envconfig()
    logger.critical(d)
    logger.critical(logging.getLevelName(logger.getEffectiveLevel()))
    return


if __name__ == '__main__':
    main()
