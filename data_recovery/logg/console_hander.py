import logging
import os
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
        level = self.logging_level_handler(level=level)
        handler.setLevel(level)
        return handler

    def get_logger(self, handler):
        """
        more like add handler
        """
        logger = logging.getLogger(__name__)
        # generic -- level should be set in handler(specific)
        # level = self.logging_level_handler()
        # has to be DEBUG, lowest in order for handler level to be effective
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        return logger

    def console_handler(self, name=None, color=True, level=None):
        """
        keep level=None, module logging-level could be changed at a level
        that is different from env
        """
        if color is True:
            return self.get_color_console_handler(name=name, level=level)

        handler = logging.StreamHandler()
        formatter = logging.Formatter(self.format_simple)
        handler.setFormatter(formatter)
        level = self.logging_level_handler(level=level)
        handler.setLevel(level)
        return handler

    def logging_level_handler(self, level=None):
        """
        logger.getEffectiveLevel()?
        level first if defined
        use env level second
        """
        if level and isinstance(level, int):
            return level
        level_env = os.environ.get(self.LOGGING_LEVEL_CONSOLE)
        if level_env:
            # environ return string(int)
            return int(level_env)
        return logging.WARN

    def setenv(self, level=logging.INFO):
        """
        for handler
        input: type int
        :rtype: int
        """
        os.environ[self.LOGGING_LEVEL_CONSOLE] = str(level)


def main():
    # console only
    # for developping
    ch = ConsoleHandler()
    # set logging-level once at env
    ch.setenv(level=logging.DEBUG)
    chander = ch.console_handler(color=True, level=None)
    logger = ch.get_logger(chander)

    d = ch.get_envconfig()
    logger.critical(d)
    logger.critical(logging.getLevelName(logger.getEffectiveLevel()))
    return


if __name__ == '__main__':
    main()
