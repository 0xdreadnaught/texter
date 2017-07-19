# texter
Simple python text bomber

*USE AT YOUR OWN RISK. I AM NOT LIABLE FOR ANYTHING YOU DO WITH THIS SCRIPT. THIS IS SIMPLY PROOF OF CONCEPT*

You need to have credentials for an smtp server for this to work
All text messages are emails. You can use reverse cell carrier lookups to find out the proper email address for a phone number
For example, an ATT number would be 123-456-7890@txt.att.net

Depending on the smtp service used there may be junk in the message, there is no way around that as it is caused by the smtp service itself.
An important note, once you start this script, that's it, the messages are sent. 
Very important note, depending on how your smtp server handles outgoing messages, each text may be received as a serparate conversation.
So if you send someone 100 messages, they will have 100 new conversations with 1 message each on their phone. 

This doesn't seem to have any practical application other than harassing people. However, this can be used for penetratino testing with slight modification.
If you setup your own smtp server, or have the ability to control the sender's address, you can modify this script to send out a single message to multiple targets in a phishing tactic.
This could also be used to test mail server sanitization, such as mass bombiing a company's email server attempting to fill up every user's inbox which would slow down or prevent business transactions.