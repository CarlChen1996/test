import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

# 设置smtplib所需的参数
# 下面的发件人，收件人是用于邮件传输的。
smtpserver = '15.73.212.81'
sender = 'carl.chen@hp.com'
# 收件人为多个收件人
receiver = ['carl.chen@hp.com','352501465@qq.com']
subject = 'Report email test'
# 通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
# subject = '中文标题'
subject = Header(subject, 'utf-8').encode()
# 构造邮件对象MIMEMultipart对象
# 下面的主题，发件人，收件人，日期是显示在邮件页面上的。
msg = MIMEMultipart('mixed')
msg['Subject'] = subject
msg['From'] = sender
# 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
msg['To'] = ";".join(receiver)
# 构造文字内容
text = """Hi, 

Your test has been completed, please refer to the attachment for details.

Best regards"""

text_plain = MIMEText(text, 'plain', 'utf-8')
msg.attach(text_plain)
# 构造图片链接
# sendimagefile = open(r'E:\PycharmProjects\test\out_html\actual_img\123.jpg', 'rb').read()
# image = MIMEImage(sendimagefile)
# image.add_header('Content-ID', '<image1>')
# image["Content-Disposition"] = 'attachment; filename="123.jpg"'
# msg.attach(image)

# 构造html
# with open("task_1.html", 'r', encoding='utf-8') as f:
#     r = f.read()
# html = """{}""".format(r)
# text_html = MIMEText(html, 'html', 'utf-8')
# text_html["Content-Disposition"] = 'attachment; filename="report.html"'
# msg.attach(text_html)

# 构造附件
sendfile = open(r'E:\PycharmProjects\test\log_module\task_1.rar', 'rb').read()
text_att = MIMEText(sendfile, 'base64', 'utf-8')
# text_att["Content-Type"] = 'application/octet-stream'
# 以下附件可以重命名成aaa.txt
text_att["Content-Disposition"] = 'attachment; filename="task_1.rar"'
# 另一种实现方式
# text_att.add_header('Content-Disposition', 'attachment', filename='1.gif')
# 以下中文测试不ok
# text_att["Content-Disposition"] = u'attachment; filename="中文附件.txt"'.decode('utf-8')
msg.attach(text_att)

# 发送邮件

smtp = smtplib.SMTP()
smtp.connect(smtpserver, 25)
# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
# smtp.set_debuglevel(1)
smtp.sendmail(sender, receiver, msg.as_string())
print('send email success')
smtp.quit()