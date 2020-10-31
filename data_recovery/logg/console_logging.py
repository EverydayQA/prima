import os
import logging
import logging.config
import colorlog
from logg.logging_common import LoggingCommon


class ConsoleLogging(LoggingCommon):

    def get_color_console_logger(self, name=None, level=None):

        formatter = colorlog.ColoredFormatter(
            self.CFORMAT_LONG,
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

        level = self.use_logging_level(level=level)
        handler.setLevel(level)

        if not name:
            name = self.get_name()
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
        return logger

    def console_logger(self, name=None, color=True, level=None):
        """
        dictconfig is not recommended, it has its own syntax
        """
        if color is True:
            return self.get_color_console_logger(name=name, level=level)

        handler = logging.StreamHandler()
        formatter = logging.Formatter(self.format_simple)
        handler.setFormatter(formatter)
        level = self.use_logging_level(level=level)
        handler.setLevel(level)

        if not name:
            name = self.get_name()
        logger = logging.getLogger(name)
        logger.addHandler(handler)
        logger.setLevel(level)

        return logger

    def use_logging_level(self, level=None):
        """
        level first if defined
        use env level second
        """
        if level and isinstance(level, int):
            return level
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


def main():
    # console only
    # for developping
    cl = ConsoleLogging()
    # set logging-level once at env
    cl.setenv_logging_level_console(logging.DEBUG)
    logger = cl.console_logger(color=False, level=None)

    logger.critical(cl.LOGGING_LEVEL_CONSOLE)
    logger.critical(os.environ.get(cl.LOGGING_LEVEL_CONSOLE))
    logger.critical(cl.LOGGING_LEVEL_FILE)
    logger.critical(os.environ.get(cl.LOGGING_LEVEL_FILE))
    logger.critical(cl.LOGGING_FILE)
    logger.critical(os.environ.get(cl.LOGGING_FILE))
    logger.info(cl.names())
    return


if __name__ == '__main__':
    main()
