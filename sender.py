import smtplib
#SERVER = "localhost"

FROM = 'sender@sender.sender'

TO = ["test@test.test"] # must be a list

SUBJECT = "Hello!"

TEXT = "This message was sent with Python's smtplib."

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP('127.0.0.1')
server.sendmail(FROM, TO, message)
server.quit()