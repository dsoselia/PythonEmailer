import emailparserpy3

#mail=emailparserpy3.emailparser("127.0.0.1", 993, "sender@sender.sender", "sender")
mail=emailparserpy3.emailparser("127.0.0.1", 993, "rc@rc.rc", "rc")
#mails=mail.get_all_emails_by_recipient_name("sender@sender.sender")
#print("sender: "+str(len(mails)))
#mails=mail.get_all_emails_by_recipient_name("test@test.test")
#print("test: "+str(len(mails)))
mails=mail.get_all_emails_by_recipient_name("rc@rc.rc")
print("rc: "+str(len(mails)))

