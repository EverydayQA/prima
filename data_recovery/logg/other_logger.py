import logging
from logg.console_hander import ConsoleHandler
from logg.file_hander import FileHandler


class OtherLogger(object):

    def logger(self, color=True, level=None, file_level=None):
        """
        with some basic information
        color for console handler
        level for console logging-leve
        file_level for FileHandler
        logfile name
        error_logname
        """
        pass
        # console only
        ch = ConsoleHandler()
        # set logging-level once at env
        ch.setenv_logging_level_console(logging.DEBUG)
        chander = ch.console_handler(color=True, level=None)

        # add console handler
        logger = ch.get_logger(chander)

        fh = FileHandler()
        # set logging-level once at env
        fh.setenv_logging_level_logfile(logging.DEBUG)
        # set logfile/error_log
        log = fh.get_logfile_basename()
        fh.setenv_logfile(log)
        fh.setenv_errlog(log)

        chander = fh.file_handler(level=None)
        # add file handler/err handler
        logger = fh.get_logger(chander)
        return logger
        raise Exception('error handler to be added')


def todo():
    print('add args to set logging config')
    print('add class to set logger')


def main():
    """
    move all these to Logger.logger()
    """
    other = OtherLogger()
    logger = other.logger()
    d = other.get_envconfig()
    logger.critical(d)
    logger.critical(logging.getLevelName(logger.getEffectiveLevel()))


if __name__ == '__main__':
    todo()
    main()
