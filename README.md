# Email Sender and Receiver with terminal and web interface


Sends receives emails from a postfix server (either local or any public imap and smtp servers that allow ssl access). The project consists of docker file running postfix server for testing purposes and codebase for recieving&amp;sending emails with attachements.

github repo [https://github.com/dsoselia/PythonEmailer](https://github.com/dsoselia/PythonEmailer)

## Important classes and functions

file attachement.py

attachment.py.send\_mail()  - receives

sender, reciever, subject, text - strings

Files - list of filesnames to be attached with the email

file emailparserpy3.py

class

emailparser (modified from hermag/PythonEmailer)

Constructor recieves

self, imap\_host,, user, pswd as strings

Imap\_port - as int;

get\_all\_emails\_by\_recipient\_name(self, recipients\_email, email\_folder\_name=&#39;inbox&#39;)

get\_last\_email\_by\_recipient\_name(self, recipients\_email, email\_folder\_name=&#39;inbox&#39;)

test.py

runs basic steps

app.py

contains flask server for web application

## Dependencies

flask server

## Demo Setup

Send email : postfix server port 25

Access email: postfix server port 993
