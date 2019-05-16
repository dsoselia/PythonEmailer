import emailparserpy3

#mail=emailparserpy3.emailparser("127.0.0.1", 993, "sender@sender.sender", "sender")
mail=emailparserpy3.emailparser("127.0.0.1", 993, "rc@rc.rc", "rc")
#mails=mail.get_all_emails_by_recipient_name("sender@sender.sender")
#print("sender: "+str(len(mails)))
#mails=mail.get_all_emails_by_recipient_name("test@test.test")
#print("test: "+str(len(mails)))
mails=mail.get_all_emails_by_recipient_name("rc@rc.rc")
print("rc: "+str(len(mails)))



last_mail=mail.get_last_email_by_recipient_name("rc@rc.rc")
#print(last_mail)
attachment=mail.get_email_attachments_by_multiple_emailfiles([last_mail])
print(attachment.keys())


for key in attachment.keys():
    with open("rec_"+key, "wb") as the_file:
        the_file.write(attachment[key]) 

