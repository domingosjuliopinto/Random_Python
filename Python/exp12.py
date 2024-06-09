import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
body='Cyclone will arrive in few days'
msg=MIMEText(body)
fromaddr="" #from email address
toaddr="" #to email address
msg['From']=fromaddr
msg['To']=toaddr
msg['Subject']="Hello Cyclone"
serv=smtplib.SMTP('smtp.gmail.com',587)
serv.starttls()
serv.login(fromaddr,"")#google/gmail code
serv.send_message(msg)
print("mail sent")
serv.quit()
