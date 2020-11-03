import logging
from logg.console_hander import ConsoleHandler
from logg.file_hander import MyFileHandler


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
        fh = MyFileHandler()
        # set logging-level once at env
        fh.setenv(level=str(level), name=name)

    @classmethod
    def error_logger(self, level=None, name=None):
        """
        with some basic information
        color for console handler
        level for console logging-leve
        file_level for FileHandler
        logfile name
        error_logname
        """

        fh = MyFileHandler()
        logger = logging.getLogger('same_name')

        for hl in logger.handlers:
            if isinstance(hl, logging.FileHandler):
                if not isinstance(hl, logging.handlers.RotatingFileHandler):
                    logger.removeHandler(logger.handlers[0])

        errhandler = fh.error_handler()
        logger.addHandler(errhandler)
        # logger.setLevel(logging.DEBUG)
        return logger

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

        fh = MyFileHandler()
        fhandler = fh.file_handler(level=level)
        logger = logging.getLogger('same_name')
        for hl in logger.handlers:
            if isinstance(hl, logging.handlers.RotatingFileHandler):
                logger.removeHandler(hl)
        logger.addHandler(fhandler)

        errhandler = fh.error_handler()
        logger.addHandler(errhandler)
        logger.setLevel(logging.DEBUG)
        return logger

    @classmethod
    def logger(self, color=True, level=None, file_level=None, name=None):
        """
        messy with multiple handlers, duplicated handers always present
        """
        # return self.file_logger()
        return self.console_logger()
        # console
        ch = ConsoleHandler()
        chandler = ch.console_handler(color=color, level=level)
        # add console handler
        logger = logging.getLogger('same_name')
        for hl in logger.handlers:
            # remove duplicated handlers
            logger.removeHandler(hl)

        logger.addHandler(chandler)
        logger.setLevel(logging.DEBUG)

        # file
        fh = MyFileHandler()
        # err handler
        errhandler = fh.error_handler()
        logger.addHandler(errhandler)

        fhandler = fh.file_handler(level=file_level)
        logger.addHandler(fhandler)
        return logger

    @classmethod
    def loggers(self):
        items = []
        items.append(self.console_logger())
        items.append(self.file_logger())
        items.append(self.error_logger())
        return items

    def log(self, method, msg):
        """
        loop method using different loggers
        """
        pass


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
