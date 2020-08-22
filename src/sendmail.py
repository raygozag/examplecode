import smtplib
from email.mime.multipart import MIMEMultipart
import sys

gmail_user = 'raygoza4@gmail.com'
gmail_password = 'diesezahlen12'

sent_from = gmail_user  
to = ['raygoza4@gmail.com', 'raygozajk@gmail.com']  
subject = "Done!"
body = 'Hey, whats up?\n\n- You'

msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = "raygozajk@gmail.com"
msg['Subject'] = 'Done'

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, msg.as_string())
    server.close()

    print 'Email sent!'
except Exception, e:
    print(e)  
    print 'Something went wrong...'