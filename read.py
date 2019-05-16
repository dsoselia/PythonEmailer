import emailparserpy3

mail=emailparserpy3.emailparser("127.0.0.1", 993, "rc@rc.rc", "rc")

last_mail=mail.get_last_email_by_recipient_name("rc@rc.rc")
attachment=mail.get_email_attachments_by_multiple_emailfiles([last_mail])
print(attachment.keys())


for key in attachment.keys():
    with open("rec_"+key, "wb") as the_file:
        the_file.write(attachment[key]) 

