import logging
from logg.logging_config import LoggingConfig
from logging.handlers import RotatingFileHandler


class FileHandler(LoggingConfig):

    def get_logger(self, handler):
        """
        more like add handler
        """
        logger = logging.getLogger(__name__)
        # generic -- level should be set in handler(specific)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger

    def error_handler(self, name=None, level=None):
        """
        dictconfig is not recommended, it has its own syntax
        """
        raise Exception('get_errlog to be coded')
        handler = RotatingFileHandler('/tmp/my_log.log', maxBytes=2000, backupCount=10)
        formatter = logging.Formatter(self.format_simple)
        handler.setFormatter(formatter)
        level = self.use_logging_level(level=level)
        handler.setLevel(level)
        return handler

    def file_handler(self, name=None, level=None):
        """
        dictconfig is not recommended, it has its own syntax
        """
        raise Exception('get_logfile to be coded')
        handler = RotatingFileHandler('/tmp/my_log.log', maxBytes=2000, backupCount=10)
        formatter = logging.Formatter(self.format_simple)
        handler.setFormatter(formatter)
        level = self.use_logging_level(level=level)
        handler.setLevel(level)
        return handler

    def use_logging_level(self, level=None):
        """
        logger.getEffectiveLevel()?
        level first if defined
        use env level second
        """
        if level and isinstance(level, int):
            return level
        level_env = self.getenv_logging_level_logfile()
        if level_env:
            return int(level_env)
        # not to set env
        # default LEVEL, not too much info
        return logging.WARN

    def getenv_logging_level_logfile(self):
        """
        str(int)
        for handler
        """
        return self.getenv_logging_level(self.LOGGING_LEVEL_FILE)

    def setenv_logging_level_logfile(self, level):
        """
        for handler
        input: type int
        :rtype: int
        """
        return self.setenv_logging_level(self.LOGGING_LEVEL_FILE, level)

    def todo(self):
        """
        seperate class for LogName()
        __name__/date/userid?
        """
        pass


def main():
    """
    """
    ch = FileHandler()
    # set logging-level once at env
    ch.setenv_logging_level_logfile(logging.DEBUG)
    # set logfile/error_log
    log = ch.get_logfile_basename()
    ch.setenv_logfile(log)
    ch.setenv_errlog(log)

    chander = ch.file_handler(level=None)
    logger = ch.get_logger(chander)

    d = ch.get_envconfig()
    logger.critical(d)
    logger.critical(logging.getLevelName(logger.getEffectiveLevel()))
    return


if __name__ == '__main__':
    main()
