import emailparserpy3

mail=emailparserpy3.emailparser("127.0.0.1", 993, "test@test.test", "test")
mails=mail.get_all_emails_by_recipient_name("test")
print(mails)
print(mail.get_email_folders())

