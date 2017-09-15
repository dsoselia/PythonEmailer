# Author: Erekle Magradze
# 11.06.2017
# contact: erekle@magradze.de

import datetime
import email
import imaplib
import os
import smtplib
import string
import sys

import dateutil.parser as parser


class emailparser(object):

    def __init__(self, imap_host, imap_port, user, pswd):
        self.imap_host = imap_host
        self.imap_port = imap_port
        self.username = user
        self.password = pswd
        self.client = imaplib.IMAP4_SSL(self.imap_host, self.imap_port)
        try:
            self.client.login(self.username, self.password)
            print("Email session has been established")
        except:
            print("Cannot communicate with the IMAP server, check connections.\n")
            sys.exit(2)

    def get_all_email_uid_by_recipient_name_before_the_date(self, plant_email_address, plant_email_cleanup_period, email_folder_name='inbox'):
        email_recipient_uid_list = []
        self.client.select(email_folder_name)
        current_time = datetime.datetime.now().replace(microsecond=0)
        before_time = current_time - datetime.timedelta(minutes=int(plant_email_cleanup_period))
        result, email_uids = self.client.uid('search', '(BEFORE %s)'%before_time.strftime("%d-%b-%Y"), '(FROM %s)'%str(plant_email_address))
        if not email_uids:
            return "Cannot fetch emails for %s before %s" % (plant_email_address, before_time.strftime("%d-%b-%Y")), email_recipient_uid_list
        else:
            for email_uid in email_uids[0].split():
                email_recipient_uid_list.append(int(email_uid.decode('UTF-8')))
        return "Retrieved %d emails to delete for %s" % (len(email_recipient_uid_list), plant_email_address), email_recipient_uid_list

    def delete_email(self, plant_email_uid_list_to_remove):
        #print(plant_email_uid_list_to_remove)
        for plant_email_uid_to_remove in plant_email_uid_list_to_remove:
            self.client.uid('STORE', str(plant_email_uid_to_remove), '+FLAGS', '(\\Deleted)')
        self.client.expunge()
        return

    def get_email_folders(self):
        # Returns list of email account folders.
        status = ""
        email_folder_list = []
        try:
            status, tmp_email_folder_list = self.client.list()
        except:
            print("Cannot retrieve the email user folder structure.\n")
            sys.exit(2)
        if status != 'OK':
            print("Failed with %s to retrieve the email folder structure.\n" % status)
            sys.exit(2)
        else:
            for item in tmp_email_folder_list:
                email_folder_list.append(item.split()[-1][1:-1])
            return status, email_folder_list
        return status, email_folder_list

    def get_last_email_by_recipient_name(self, recipients_email, email_folder_name='inbox'):
        email_recipient_uid = 0
        self.client.select(email_folder_name)
        #result, email_uids = self.client.uid('search', None, "ALL")
        result, emails_uids = self.client.uid('search', None, '(FROM "%s")' % recipients_email)
        if not emails_uids:
            print("No emails with matching recipient email address %s were found" % recipients_email)
            # sys.exit(2)
        else:
            last_email_uid = emails_uids[0].split()[-1]
            resp, data = self.client.uid('fetch', '%d' % int(last_email_uid), '(RFC822)')
            # print data
            #email_body = data[0][1]
            #m = email.message_from_string(email_body)
            # return m
            return email.message_from_bytes(data[0][1])
        print("No emails with matching recipient name %s were found" % recipient_name)
        # sys.exit(2)
        return

    def get_all_emails_by_recipient_name(self, recipients_email, email_folder_name='inbox'):
        self.client.select(email_folder_name)
        # result, email_uids = self.client.uid('search', None, "ALL")
        result, email_uids = self.client.uid('search', None, '(FROM "%s")' % recipients_email)
        # print email_uids
        emails_list = []
        if not email_uids:
            print("No emails with matching recipient email address %s were found" % recipients_email)
            return emails_list
            # sys.exit(2)
        else:
            for emailid in email_uids[0].split():
                resp, data = self.client.uid('fetch', '%d' % int(emailid), '(RFC822)')
                # emails_list.append(email.message_from_string(data[0][1]))
                emails_list.append(email.message_from_bytes(data[0][1]))
        return emails_list

    def get_emails_by_uids_list(self, uids_list):
        emails_list_by_uid = []
        for email_uid in uids_list:
            resp, data = self.client.uid('fetch', '%d' % int(email_uid), '(RFC822)')
            # print data[0], type(data[0])
            if data[0] != None:
                # emails_list_by_uid.append(email.message_from_string(data[0][1]))
                emails_list_by_uid.append(email.message_from_bytes(data[0][1]))
            else:
                continue
        if not emails_list_by_uid:
            print("Could not fetch emails by the given list of uids, check uid validity")
            # sys.exit(2)
        else:
            pass
        return emails_list_by_uid

    def get_email_by_uid(self, email_uid):
        try:
            resp, data = self.client.uid('fetch', '%d' % int(email_uid), '(RFC822)')
            if data[0] == None:
                return None
            else:
                pass
        except:
            print("problem with fetching the email based on the email ID ", email_uid)
        # print(email.message_from_bytes(data[0][1]))
        # return email.message_from_string(data[0][1])
        return email.message_from_bytes(data[0][1])

    def get_last_email_uid_by_recipient_name(self, recipients_email, email_folder_name='inbox'):
        email_uids_list = []
        last_uid_of_email_recipient = ""
        self.client.select(email_folder_name)
        #result, email_uids = self.client.uid('search', None, "ALL")
        result, email_uids = self.client.uid('search', None, '(FROM "%s")' % recipients_email)
        if not email_uids:
            print("No emails with matching recipient name %s were found" % recipients_email)
            sys.exit(2)
        else:
            pass
        return str(email_uids[0].split()[-1].decode('UTF-8'))

    def get_all_email_uid_by_recipient_name(self, recipients_email, email_folder_name='inbox'):
        self.client.select(email_folder_name)
        email_uids_list = []
        #result, email_uids = self.client.uid('search', None, "ALL")
        result, email_uids = self.client.uid('search', None, '(FROM "%s")' % recipients_email)
        if not email_uids:
            print("No emails with matching recipient name %s were found" % recipients_email)
            sys.exit(2)
        else:
            pass
        for email_uid in email_uids[0].split():
            email_uids_list.append(str(email_uid.decode('UTF-8')))
        return email_uids_list

    def get_email_attachment_by_emailfile(self, emailfile, plantID):
        m = emailfile
        filename = ""
        attachment_content = ""
        if m.get_content_maintype() != 'multipart':
            print("Email does not contain any attachment.")
            sys.exit(2)
        else:
            pass
        for part in m.walk():
            if part.get_content_maintype() == 'multipart' and part.get('Content-Disposition') is None:
                continue
            else:
                # if part.get('Content-Disposition') is None:
                #    continue
                filename = part.get_filename()
                if filename is not None:
                    attachment_content = part.get_payload(decode=True)
                else:
                    continue
                # Fetching the timestamp from the email body
                email_body_text = emailfile.get_payload()[0].get_payload()
                if type(email_body_text) is str:
                    #email_body_text=','.join(str(l) for l in email_body_text)
                    try:
                        email_body_text_list = email_body_text.split(" ")[-4:]
                        timestamp = " ".join(str(itm) for itm in email_body_text_list)
                        timestamp = timestamp[:-1]
                        email_timestamp = parser.parse(timestamp)
                        #timenow = datetime.datetime.now().replace(microsecond=0)
                        #utctimenow = datetime.datetime.utcnow().replace(microsecond=0)
                        #UTChourstonow = int(round((timenow - utctimenow).seconds / 3600.0))
                        #email_timestamp = email_timestamp + datetime.timedelta(hours=UTChourstonow)
                        time_now = datetime.datetime.strftime(email_timestamp, "%Y-%m-%d_%H:%M:%S")
                    except:
                        time_now = str(datetime.datetime.now()).replace(" ", "_")
                else:
                    time_now = str(datetime.datetime.now()).replace(" ", "_")
                if len(filename.split(".")) == 2 and "bz2" not in filename and str(filename.split(".")[0]).isalpha():
                    #filename = "%s_%s.%s" % (str(filename.split(".")[0]), time_now, str(filename.split(".")[1]))
                    filename = "%s_%s.csv" % (plantID, time_now)
                else:
                    pass
        # print "filename ---> ", filename
        return filename, attachment_content

    def get_email_attachments_by_multiple_emailfiles(self, emailfiles_list):
        m_list = emailfiles_list
        attachment_dictionary = {}
        for m in m_list:
            filename = ""
            attachment_content = ""
            if m.get_content_maintype() != 'multipart':
                print("Email does not contain any attachment.")
                continue
            else:
                pass
            # Fetching the timestamp from the email body
            email_body_text = m.get_payload()[0].get_payload()
            if type(email_body_text) is str:
                try:
                    email_body_text_list = email_body_text.split(" ")[-4:]
                    timestamp = " ".join(str(itm) for itm in email_body_text_list)
                    timestamp = timestamp[:-1]
                    email_timestamp = parser.parse(timestamp)
                    timenow = datetime.datetime.now().replace(microsecond=0)
                    utctimenow = datetime.datetime.utcnow().replace(microsecond=0)
                    UTChourstonow = int(round((timenow - utctimenow).seconds / 3600.0))
                    email_timestamp = email_timestamp + datetime.timedelta(UTChourstonow)
                    time_now = datetime.datetime.strftime(email_timestamp, "%Y-%m-%d_%H:%M:%S")
                except:
                    time_now = str(datetime.datetime.now()).replace(" ", "_")
            else:
                time_now = str(datetime.datetime.now()).replace(" ", "_")
            for part in m.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                filename = part.get_filename()
                if filename is not None:
                    attachment_content = part.get_payload(decode=True)
                    if len(filename.split(".")) == 2 and "bz2" not in filename and str(filename.split(".")[0]).isalpha():
                        filename = "%s_%s.%s" % (str(filename.split(".")[0]), time_now, str(filename.split(".")[1]))
                    else:
                        pass
                    attachment_dictionary[filename] = attachment_content
                else:
                    continue
        return attachment_dictionary

    def quitconn(self):
        self.client.logout()
        print("Disconnected")
        return
