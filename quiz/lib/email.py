#!/usr/bin/python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class MimeSend(object):
    def __init__(self, subject, tos, froms, msg_txt, msg_html, smtp_host, atts, debug, run)
        self.tos = tos
        self.froms = froms
        self.subject = subject
        self.smtp_host = smtp_host
        self.msg_txt = msg_txt
        self.msg_html = msg_html
        self.atts = atts
        self.debug = debug
        self.run = run

    def mime_msg_wrapper(self):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = self.froms
        msg['To'] = self.tos
        part1 = MIMEText(self.text_str, 'plain')
        part2 = MIMEText(self.html_str, 'html')
        msg.attach(part1)
        msg.attach(part2)
        return msg

    @property
    def text_str(self):
        text = 'are you texter'
        return text
    @property
    def html_str(self):
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
        s.sendmail(self.tos, self.froms, self.msg.as_string())
        s.quit()

def main():
    # parameters
    mime_send = MimeSend()
    mime_send.send_smtp()


# argspase - for command line
if __name__ == 'main':
    main()

