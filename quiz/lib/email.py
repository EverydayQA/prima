#!/usr/bin/python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse

class MimeSend(object):
    def __init__(self, *args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    @property
    def logger(self):
        name = os.path.splitext(os.path.basename(__file__))[0] + "." + self.__class__.__name__ 
        logger = logging.getLogger(name)
        level = self.kwargs.get('level', 30)
        logger.setLevel(level)
        el  = logger.getEffectiveLevel()
        line = 'logger level is: {0} args cls {1} EffectiveLevel {2}\n'.format(logger.level, name, el)
        logger.debug(line)
        return logger 

    @property
    def email_to(self):
        return self.kwargs.get('to', None)

    @property
    def email_from(self):
        return self.kwargs.get('from', None)

    @property
    def subject(self):
        return self.kwargs.get('subject', None)

    @property
    def attachments(self):
        if not self.args:
            return []
        atts = []
        for arg in self.args:
            if os.path.isfile(arg):
                atts.append(arg)
        return atts

    @property
    def smtp_server(self):
        return self.kwargs.get('smtp_server', None)

    @property
    def to_send(self):
        return self.kwargs.get('send', None)

    def mime_msg_wrapper(self):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = self.email_from
        msg['To'] = self.email_to
        part1 = MIMEText(self.text_str, 'plain')
        part2 = MIMEText(self.html_str, 'html')
        msg.attach(part1)
        msg.attach(part2)
        return msg

    @property
    def text_str(self):
        # for test only
        text = 'are you texter'
        return text

    @property
    def html_str(self):
        # for test only
        html = """\
        <html>
            <head></head>
            <body>
            <p>
            are you htmler?
            </p>
            </body>
        </html>
        """
        return html

    def send_smtp(self):
        s = smtplib.SMTP(self.smtp_host)
        s.sendmail(self.email_to, self.email_from, self.msg.as_string())
        s.quit()

def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--level', type=int, default=20, help='logging level')
    parser.add_argument('-t', '--to', type=str, default='', help='email address to send')

    args, args_extra = parser.parse_known_args(sys.argv[1:] )
    return args, args_extra

def main():
    args, args_extra = init_args()
    name = os.path.splitext(os.path.basename(__file__))[0]
    logger = logging.getLogger(name)

    logger.setLevel(args.logging)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(args.logging)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.propagate = False

    # sys.args[0] as text attachment
    mime_send = MimeSend(sys.argv[0], to="joe", from='joe', subject='test subject')
    mime_send.send_smtp()

# argspase - for command line
if __name__ == 'main':
    main()

