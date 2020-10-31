import logging
import logging.config
import colorlog
from logg.logging_config import LoggingConfig


class ConsoleHandler(LoggingConfig):

    def get_color_console_handler(self, name=None, level=None):

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
        return handler

    def get_logger(self, handler):
        """
        more like add handler
        """
        logger = logging.getLogger(__name__)
        # generic -- level should be set in handler(specific)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger

    def console_handler(self, name=None, color=True, level=None):
        """
        dictconfig is not recommended, it has its own syntax
        """
        if color is True:
            return self.get_color_console_handler(name=name, level=level)

        handler = logging.StreamHandler()
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
        level_env = self.getenv_logging_level_console()
        if level_env:
            return int(level_env)
        # not to set env
        # default LEVEL, not too much info
        return logging.WARN

    def getenv_logging_level_console(self):
        """
        str(int)
        for handler
        """
        return self.getenv_logging_level(self.LOGGING_LEVEL_CONSOLE)

    def setenv_logging_level_console(self, level):
        """
        for handler
        input: type int
        :rtype: int
        """
        return self.setenv_logging_level(self.LOGGING_LEVEL_CONSOLE, level)


def main():
    # console only
    # for developping
    ch = ConsoleHandler()
    # set logging-level once at env
    ch.setenv_logging_level_console(logging.DEBUG)
    chander = ch.console_handler(color=True, level=None)
    logger = ch.get_logger(chander)

    d = ch.get_envconfig()
    logger.critical(d)
    logger.critical(logging.getLevelName(logger.getEffectiveLevel()))
    return


if __name__ == '__main__':
    main()
