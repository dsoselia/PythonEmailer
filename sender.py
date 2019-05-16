import smtplib
#SERVER = "localhost"
FROM = 'sender@sender.sender'
#FROM = 'sender@sender.sender'
#FROM = 'rc@rc.rc'

TO = ["rc@rc.rc"] # must be a list

SUBJECT = "Hello! RC"

TEXT = "This is test Email."

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

#server = smtplib.SMTP('95.104.92.215',25)
server = smtplib.SMTP('127.0.0.1',25)
server.sendmail(FROM, TO, message)
server.quit()
