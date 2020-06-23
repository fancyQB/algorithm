import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


mail_server = 'smtp.163.com'
mail_port = 25
sender =  '15926440508@163.com'
passwd = 'ZWUESNPGKYJEPTWG'
receviers = '1365339838@qq.com'


message = MIMEMultipart()
message.attach(MIMEText('nihao', 'plain', 'utf-8'))
message['From'] = sender
message['To'] = receviers
message['subject'] = '你好'
att1 = MIMEText(open('D:/python_work_place/code/Personal_information.xlsx', 'rb').read(), 'base64', 'utf-8')
att1['Content-Type'] = 'application/octet-stream'
att1['Content-Disposition'] = 'attachment; filename=' + 'Personal_information.xlsx'
message.attach(att1)
smtp_obj = smtplib.SMTP()
smtp_obj.connect(mail_server, mail_port)
smtp_obj.login(sender, passwd)
smtp_obj.sendmail(sender, [receviers], message.as_string())
print('success!')
