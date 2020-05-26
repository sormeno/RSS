import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import logging
logger = logging.getLogger('RSS_feed.mail')

class SMTP:

    def __init__(self, host, port, msg_from, password):
        self.s = smtplib.SMTP(host=host, port=port)
        self.msg_from = msg_from
        self.s.starttls()
        try:
            self.s.login(self.msg_from, password)
            logger.info(f'Successful login to {self.msg_from}')
        except:
            logger.error(f'Failed to login to {self.msg_from}', exc_info=True)
            sys.exit()



    def close(self):
        try:
            self.s.quit()
            logger.info(f'Mail login to {self.msg_from} successfully closed')
        except:
            logger.warning(f'Mail login to {self.msg_from} has not been closed')


    def send_email(self,msg_to, msg_subject, msg_content = None, msg_html_content = None):
        msg = MIMEMultipart()
        msg_content = msg_html_content if msg_html_content else msg_content
        msg_type = 'html' if msg_html_content else 'plain'

        msg['From'] = self.msg_from
        msg['To'] = msg_to
        msg['Subject'] = msg_subject
        logger.info(f'Preparing message \'{msg["Subject"]}\' to \'{msg["To"]}\' from \'{msg["From"]}\'. Message type: {msg_type}')
        msg.attach(MIMEText(msg_content, msg_type))
        logger.info(f'Message content attached to message')
        self.s.send_message(msg)
        logger.info(f'Message to \'{msg["To"]}\' has been sent')
        del msg


