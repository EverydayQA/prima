import os
import logging
import logging.config
import time


class ConstLoggingConfig(object):
    LOGGING_LEVEL_FILE = 'LOGGING_LEVEL_FILE'
    LOGGING_LEVEL_CONSOLE = 'LOGGING_LEVEL_CONSOLE'
    LOGGING_FILE = 'LOGGING_FILE'
    INFO = 'INFO'
    DEBUG = 'DEBUG'
    WARN = 'WARN'
    CRITICAL = 'CRITICAL'
    ERROR = 'ERROR'


class LoggingConfig(ConstLoggingConfig):

    """
    LOGGING_LEVEL_FILE
    who is responsible to set LOGGING_LEVEL_CONSOLE env?
    who will use the level?
    what about multiple clis?
    """

    @property
    def format_simple(self):
        return '%(name)-12s: %(levelname)-8s %(message)s'

    @property
    def format_verbose(self):
        return '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'

    def d_level(self):
        """
        do not know how to set level as variable, add this
        """
        d = {}
        d[logging.INFO] = self.INFO
        d[logging.DEBUG] = self.DEBUG
        d[logging.WARN] = self.WARN
        d[logging.CRITICAL] = self.CRITICAL
        d[logging.ERROR] = self.ERROR
        return d

    def console_only_config(self):
        """
        NOT to set env level
        """
        level_env = self.get_console_level()
        if level_env:
            level = int(level_env)
        else:
            # not to set env
            # level = self.set_env_console_level(str(level))
            # but do set logger level of the module
            # default LEVEL, not too much info
            level = logging.WARN

        d = self.d_level()
        levelstr = d.get(level, logging.WARN)

        LOGGING = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'console_format': {
                    'format': self.format_simple, }, },
            'handlers': {
                'console': self.console_handler(levelstr), },

            'root': {
                'level': levelstr,
                'handlers': ['console'], },
        }
        return LOGGING

    def file_only_config(self, level=logging.DEBUG, logfile=None):
        if not logfile:
            # have to be special name
            # raise exception?
            logfile = '/tmp/logfile'

        d = self.d_level()
        levelstr = d.get(level, logging.DEBUG)

        LOGGING = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'file_format': {
                    'format': self.format_verbose, }, },
            'handlers': {
                'logfile': self.logfile_handler(logfile), },

            'root': {
                'level': levelstr,
                'handlers': ['logfile'], },
        }
        return LOGGING

    def both_config(self, level=logging.DEBUG, logfile=None):
        if not logfile:
            logfile = '/tmp/logfile'

        d = self.d_level()
        levelstr = d.get(level, logging.DEBUG)

        LOGGING = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'console_format': {
                    'format': self.format_simple, },
                'file_format': {
                    'format': self.format_verbose, }, },
            'handlers': {
                'console': self.console_handler(levelstr),
                'logfile': self.logfile_handler(logfile), },

            'root': {
                'level': 'INFO',
                'handlers': ['console', 'logfile'], },
        }
        return LOGGING

    def console_handler(self, levelstr):
        d = {'class': 'logging.StreamHandler',
             'level': levelstr,
             'formatter': 'console_format', }
        return d

    def logfile_handler(self, logfile):
        d = {'class': 'logging.FileHandler',
             'formatter': 'file_format',
             'filename': logfile,
             'mode': 'w'}
        return d

    def get_logfile_level(self):
        """
        int
        """
        level = os.environ.get(self.LOGGING_LEVEL_FILE)
        if level:
            return level
        return self.set_level(logging.INFO)

    def get_console_level(self):
        """
        str(int)
        """
        level = os.environ.get(self.LOGGING_LEVEL_CONSOLE)
        if level:
            return level
        return None

    def set_env_logfile_level(self, level):
        """
        input: type str(int)
        :rtype: int(str)
        """
        if not isinstance(level, int):
            print(level)
            raise Exception('set logging level must be int')
        os.environ[self.LOGGING_LEVEL_FILE] = level
        return int(level)

    def set_env_console_level(self, level):
        """
        input: type str(int)
        :rtype: int(str)
        """
        os.environ[self.LOGGING_LEVEL_CONSOLE] = str(level)
        return int(level)


def get_console_logger(name, level=None):
    """
    The first cli will call this with level defined
    other modules will just call this func without level
    default: console logger
    """
    lc = LoggingConfig()
    if level and isinstance(level, int):
        # set env
        lc.set_env_console_level(level)
    dc = lc.console_only_config()
    logging.config.dictConfig(dc)
    logging.warning('get_logger %s', time.asctime())
    logger = logging.getLogger(name)
    return logger


def get_logger_both(name, level=logging.INFO, logfile=None):
    """
    This will use if env level if set
    else logging.INFO
    default: console logger
    """
    lc = LoggingConfig()
    dc = lc.both_config(level=level, logfile='/tmp/helo')
    logging.config.dictConfig(dc)
    logging.warning('get_logger %s', time.asctime())
    logger = logging.getLogger(name)
    return logger


def main():
    # console only
    logger = get_console_logger(__name__, level=logging.WARN)
    logger.warning('logger')
    logger.info('info')
    logger.debug('debug')
    logger.warning('warn')
    logger.error('error')
    lc = LoggingConfig()
    logger.critical(lc.LOGGING_LEVEL_CONSOLE)
    logger.critical(os.environ.get(lc.LOGGING_LEVEL_CONSOLE))

    logger.critical(lc.d_level())
    return

    # not to use this way, use get_logger()
    dc = lc.both_config(level=logging.INFO, logfile='/tmp/helo')
    logging.config.dictConfig(dc)
    logging.warning('The local time is %s', time.asctime())
    logger = logging.getLogger(__name__)
    logger = get_logger_both(__name__, logfile=None)
    logger.critical('get_logger')


if __name__ == '__main__':
    main()
