from imap_tools import MailBox, Q

# get list of email subjects from INBOX folder
with MailBox('imap.gmail.com').login('ary.rpi6@gmail.com', 'Google@2018') as mailbox:
    subjects = [msg.subject for msg in mailbox.fetch()]

# get list of email subjects from INBOX folder - equivalent verbose version
mailbox = MailBox('imap.mail.com')
mailbox.login('test@mail.com', 'password', initial_folder='INBOX')  # or mailbox.folder.set instead 3d arg
subjects = [msg.subject for msg in mailbox.fetch(Q(all=True))]
mailbox.logout()
