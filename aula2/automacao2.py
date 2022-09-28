# import the smtplib module. It should be included in Python by default
import smtplib
# set up the SMTP server
s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.starttls()
s.login('marleyprojetos@outlook.com', 'lM94373043@')

import smtplib
import time

server = smtplib.SMTP_SSL('host', port)
server.ehlo()
server.login("marleyprojetos@outlook.com", "lM94373043@")

server.ehlo()

print ('server working fine')

time.sleep(5)

sender = "marleyprojetos@outlook.com"

receivers = ["leorieger17@gmail.com"]

subject = "SMTP e-mail Test" 

msg = "This is an automated message being sent by Python. Python is the mastermind behind    this."

server.sendmail(sender, receivers, subject, msg)

print ('sending email to outlook')

server.quit()