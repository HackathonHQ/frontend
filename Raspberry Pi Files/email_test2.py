import smtplib
import imaplib

smtpUser = input('Your Email?? ')
smtpPass = input('Pwd? ')

toAdd = input("To Address: ")
fromAdd = smtpUser

subject = input("Subject: ")
header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
body = input("Body: ")

s = smtplib.SMTP('smtp.gmail.com',587)

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser, smtpPass)
s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

s.quit
