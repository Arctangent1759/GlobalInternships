import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = "gib.noreply@gmail.com"
gmail_pwd = "arugula1717"

def mail(to, subject, text):
	msg = MIMEMultipart()

	msg['From'] = gmail_user
	msg['To'] = to
	msg['Subject'] = subject

	msg.attach(MIMEText(text))

	mailServer = smtplib.SMTP("smtp.gmail.com", 587)
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.ehlo()
	mailServer.login(gmail_user, gmail_pwd)
	mailServer.sendmail(gmail_user, to, msg.as_string())
	# Should be mailServer.quit(), but that crashes...
	mailServer.close()
