import smtplib
import sqlite3
gmail_user = 'VirtualHealthTsec'
gmail_password = 'Bhavesh123'
conn = sqlite3.connect('applicant_database.db')
c = conn.cursor()
c.execute("SELECT *,oid FROM Applicant")
records = c.fetchall()
sent_from = gmail_user
to = [record[1] for record in records]
subject = 'Meeting Request Accepted'
body = 'Congratulitons!\nYour meeting is accepted by Virtual Health Assistant\nThe Meeting Link is - https://meet.google.com/kvd-tsvd-dqp'

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
