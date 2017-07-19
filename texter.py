#!/usr/bin/python
import smtplib
server = smtplib.SMTP('smtp.sendgrid.net', 587)
server.login("fakebadguy", "123qweqwe")
msg = "YOU just use 'OP 1' AND IT FIXES EVERYTHING ..."
loopit = True
i = 0
while loopit:
    server.sendmail("123-123-1234", "6179557130@txt.att.net", msg)
    i+=1
    if i == 2: #number of times to loop
        loopit = False

