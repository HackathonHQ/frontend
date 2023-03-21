import smtplib

smtpUser = 'ary.rpi6@gmail.com'
smtpPass = 'Google@18'

toAdd = input('To: ')
ccAdd = input('CC, Use commas for more than one: ')
toAdd = toAdd+', '+ccAdd
fromAdd = smtpUser

subject = input('Sub: ')
header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
body = input('What?:')

print (header + '\n' + body)

s = smtplib.SMTP('smtp.gmail.com',587)

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser, smtpPass)
s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

s.quit
input('\nPress ENTER to exit')
