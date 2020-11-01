import logging
from logg.console_hander import ConsoleHandler
from logg.file_hander import FileHandler


class OtherLogger(object):

    @classmethod
    def console_logger(self, color=True, level=None):
        """
        console only logger
        """
        # console only
        ch = ConsoleHandler()
        chander = ch.console_handler(color=color, level=level)
        # add console handler
        logger = ch.get_logger(chander)
        return logger

    @classmethod
    def setenv_console(self, level=None):
        """
        # set logging-level once at env
        # set should be seperated and only at cli once
        """
        ch = ConsoleHandler()
        ch.setenv(level=str(level))

    @classmethod
    def setenv_file(self, level=None, name=None):
        fh = FileHandler()
        # set logging-level once at env
        fh.setenv(level=str(level), name=name)

    @classmethod
    def file_logger(self, level=None, name=None):
        """
        with some basic information
        color for console handler
        level for console logging-leve
        file_level for FileHandler
        logfile name
        error_logname
        """

        fh = FileHandler()
        chander = fh.file_handler(level=None)
        # add file handler
        logger = fh.get_logger(chander)

        errhandler = fh.error_handler()
        # add err handler
        logger.addHandler(errhandler)

        return logger

    @classmethod
    def logger(self, color=True, level=None, file_level=None, name=None):
        """
        """
        # console
        ch = ConsoleHandler()
        chandler = ch.console_handler(color=color, level=None)
        # add console handler
        logger = logging.getLogger(__name__)
        logger.addHandler(chandler)
        logger.setLevel(logging.DEBUG)

        # file
        fh = FileHandler()
        fhandler = fh.file_handler(level=file_level)
        # add file handler
        logger.addHandler(fhandler)
        # err handler
        errhandler = fh.error_handler()
        # add err handler
        logger.addHandler(errhandler)
        return logger


def main():
    """
    move all these to Logger.logger()
    """
    OtherLogger.setenv_console(level=logging.DEBUG)
    clogger = OtherLogger.console_logger()
    clogger.info('console logger')

    OtherLogger.setenv_file(level=logging.DEBUG, name=None)
    flogger = OtherLogger.file_logger()
    flogger.info('file logger')


if __name__ == '__main__':
    main()
