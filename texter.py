#!/usr/bin/python
import smtplib
server = smtplib.SMTP('YOURSMTPSERVERIP', YOURSMPTSERVERPORT)
server.login("USERNAME", "PASSWORD")
msg = "PUT YOUR MESSAGE HERE"
loopit = True
i = 0
while loopit:
    server.sendmail("SOURCE-NUMBER-HERE", "TARGETEMAILHERE", msg)
    i+=1
    if i == 2: #number of times to loop
        loopit = False

