#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr
# 格式化邮件地址


def sendMail(body):
    smtp_server = '15.73.212.81'
    from_mail = 'carl.chen@hp.com'
    to_mail = ['carl.chen@hp.com', '352501465@qq.com']
    # 构造一个MIMEMultipart对象代表邮件本身
    msg = MIMEMultipart()
    # Header对中文进行转码
    msg['From'] = from_mail
    msg['To'] = ','.join(to_mail)
    msg['Subject'] = Header('监控', 'utf-8').encode()
    msg.attach(MIMEText(body, 'html', 'utf-8'))
    try:
        s = smtplib.SMTP()
        s.connect(smtp_server, "25")
        # s.login(from_mail, mail_pass)
        s.sendmail(from_mail, to_mail, msg.as_string())  # as_string()把MIMEText对象变成str
        s.quit()
    except smtplib.SMTPException as e:
        print("Error: %s" % e)


if __name__ == "__main__":
    with open("task_1.html", 'r', encoding='utf-8') as f:
        r = f.read()
    html = """{}""".format(r)
    # body = """
    # <h1>测试邮件</h1>
    # <h2 style="color:red">This is a test</h1>
    # """
    sendMail(html)
