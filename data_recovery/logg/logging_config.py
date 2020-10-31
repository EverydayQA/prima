import os
import logging
import logging.config
import colorlog


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
    LOGFORMAT = "%(log_color)s - %(asctime)s - %(name)-12s - %(levelname)s - %(message)s",

    @property
    def format_simple(self):
        # return self.LOGFORMAT
        return '%(name)-12s: %(levelname)-8s %(message)s'

    @property
    def format_verbose(self):
        return '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'

    def get_logfile_xxxxlevelxxx(self):
        return self.getenv_logging_level(self.LOGGING_LEVEL_FILE)

    def getenv_logging_level(self, field):
        """
        int
        """
        level = os.environ.get(field)
        if level:
            return level
        return logging.INFO

    def setenv_logging_level_file(self, level):
        return self.setenv_logging_level(self.LOGGING_LEVEL_FILE,  level)

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


class ConsoleLogging(LoggingCommon):

    def get_color_console_logger(self, name):
        level = self.use_logging_level()

        formatter = colorlog.ColoredFormatter(
            "%(log_color)s[%(asctime)s %(levelname)-8s%(module)s]%(reset)s "
            "%(white)s%(message)s",
            datefmt="%H:%M:%S",
            reset=True,
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red',
            })

        handler = colorlog.StreamHandler()
        handler.setFormatter(formatter)
        handler.setLevel(level)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
        return logger

    def console_logger(self, name):
        """
        dictconfig is not recommended, it has its own syntax
        """
        level = self.use_logging_level()
        handler = logging.StreamHandler()
        formatter = logging.Formatter(self.format_simple)
        handler.setFormatter(formatter)
        handler.setLevel(level)

        logger = logging.getLogger(name)
        logger.addHandler(handler)
        logger.setLevel(level)

        return logger

    def use_logging_level(self):
        level_env = self.getenv_logging_level_console()
        if level_env:
            return int(level_env)
        # not to set env
        # default LEVEL, not too much info
        return logging.WARN

    def getenv_logging_level_console(self):
        """
        str(int)
        """
        return self.getenv_logging_level(self.LOGGING_LEVEL_CONSOLE)

    def setenv_logging_level_console(self, level):
        """
        input: type int
        :rtype: int
        """
        return self.setenv_logging_level(self.LOGGING_LEVEL_CONSOLE, level)


def console_logger(name, color=True, level=None):
    """
    The first cli will call this with level defined
    other modules will just call this func without level
    default: console logger
    """
    cl = ConsoleLogging()
    if level and isinstance(level, int):
        # set logging-level once at env
        cl.setenv_logging_level_console(level)
    if color is True:
        return cl.get_color_console_logger(name)
    return cl.console_logger(name)


def main():
    # console only
    logger = console_logger(__name__, color=True, level=logging.DEBUG)
    logger.warning('logger')
    logger.info('info')
    logger.debug('debug')
    logger.warn('warn')
    logger.error('error')

    # for developping
    cl = ConsoleLogging()
    logger.critical(cl.LOGGING_LEVEL_CONSOLE)
    logger.critical(os.environ.get(cl.LOGGING_LEVEL_CONSOLE))
    logger.critical(cl.LOGGING_LEVEL_FILE)
    logger.critical(os.environ.get(cl.LOGGING_LEVEL_FILE))
    logger.critical(cl.LOGGING_FILE)
    logger.critical(os.environ.get(cl.LOGGING_FILE))

    return


if __name__ == '__main__':
    main()
