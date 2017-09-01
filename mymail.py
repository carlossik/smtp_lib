
import email.base64mime
'''
import smtplib
from smtplib import SMTP
with SMTP("smtp.office365.com:587 ") as smtp:
    print(smtp.noop())

from email.mime.text import MIMEText


with open('mytext.txt','r') as fp:
    msg = MIMEText(fp.read())
    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'The contents of %s'
    msg['From'] = 'carlos.attafuah@theexchangelab.com'
    msg['To'] = 'carlossik@gmail.com'

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('smtp.office365.com:587')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
    '''
#***************************************************************************
'''
from smtplib import SMTP
import datetime
import socket

debuglevel = 0

smtp = SMTP()
smtp.set_debuglevel(debuglevel)
try:

  smtp.connect('smtp.office365.com:587', 26)
  smtp.login('carlos.attafuah@theexchangelab.com', 'Welcome123!')
except socket.gaierror:
    print('ignoring failed address lookup')
from_addr = "Carlos Attafuah <carlos.attafuah@theexchangelab.com>"
to_addr = "carlos.attafuah@theexchangelab.com"

subj = "hello"
date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

message_text = "Hello\nThis is a mail from your server\n\nBye\n"

msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (from_addr, to_addr, subj, date, message_text)


smtp.sendmail(from_addr, to_addr, msg)
smtp.quit()
'''
import smtplib
from smtplib import SMTP
import datetime
import socket
from email.mime.text import MIMEText
msg = MIMEText
#server = smtplib.SMTP('smtp.gmail.com')
server = smtplib.SMTP('smtp.office365.com:587')
server.starttls()
server.login('Carlos.Attafuah@theexchangelab.com','Welcome123!')
msg['Subject'] = "msg.channel"
msg['From'] = ('from')
msg['To'] = ('to')
server.sendmail(msg.get('From'),msg["To"],msg.as_string())
server.quit()