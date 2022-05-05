import smtplib
import sqlite3

gmail_user = 'pharatebhavesh6@gmail.com'
gmail_password = 'Bhavesh1472p'
conn = sqlite3.connect('applicant_database.db')
c = conn.cursor()
c.execute("SELECT *,oid FROM Applicant")
records = c.fetchall()

sent_from = gmail_user
to = [record[1] for record in records]
subject = 'Meeting request rejected'
body = 'Sorry,our doctors are busy right now, we hope to catch with you later'

email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)
