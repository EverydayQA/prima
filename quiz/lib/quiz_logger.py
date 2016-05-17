
import logging

# logging level?
# logging to file if kwargs define a filename

class QuizLogger(object):
    def __init__(self, **kwargs):
        if kwargs.get('name'):
            self.name = kwargs['name']
        else:
            self.name = __name__
        if kwargs.get('level'):
            self.level = kwargs['level']
        else:
            self.level = logging.DEBUG

        if kwargs.get('logname'):
            self.logname = kwargs['logname']
        else:
            self.logname = None


    @property
    def logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)
        
        ch  = logging.StreamHandler()
        ch.setLevel(self.level)
        formatter = logging.Formatter("%(asctime)s - {0}- %(levelname)s - %(message)s".format(self.name))
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        # add file handler if logname is defined
        if self.logname:
            fh  = logging.FileHandler(self.logname)
            fh.setFormatter(formatter)
            logger.addHandler(fh)
        return logger

        

