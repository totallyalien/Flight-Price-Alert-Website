import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

html_body = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
  
</body>
</html>"""

class MailAlert:
    def __init__(self, mail, password) -> None:
        self.mail=mail
        self.password=password
        self.msg = MIMEMultipart('alternative')
        self.msg['From'] = self.mail
        



    def send_mail(self,from_,to_,past,ltp,to_mail):
        self.msg['To'] = to_mail
        self.msg['Subject'] = f"Your tracked route : {from_} to {to_} flight fare has changed from {past} to {ltp} "
        self.connection = smtplib.SMTP("smtp.gmail.com")
        self.connection.starttls()
        self.body=MIMEText(html_body, 'html')    
        self.msg.attach(self.body)
        self.connection.login(user=self.mail,password=self.password)
        self.connection.sendmail(from_addr=self.mail,to_addrs=self.mail,msg=self.msg.as_string())
        self.connection.close()



