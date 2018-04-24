#--------------------------------------------------
#!/usr/bin/env python
#-*-coding:utf-8 -*-
#Time:2018/4/23  17:06
#Author:Kevin Hon
#--------------------------------------------------

'''这部分代码是用来实现发送测试报告的功能，带附件，使用的是非加密的方式发信的实现方式'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 定义发邮件的各类基础参数,使用公司邮箱发信给QQ邮箱
smtpserver = "smtp.cyberzone.cn"
port = 25
sender = "hanguolong@cyberzone.cn"
pwd = "jing-21"
receiver = "185983895@qq.com" #单人收件
# receiver = ["185983895@qq.com","858198672@qq.com"] #多人收件

# 带附件的写信模板
msg = MIMEMultipart()
msg['Subject'] = 'James harden is on fire today ！'
msg['From'] = sender
msg['To'] = receiver    #单人收件
# msg['To'] = ";".join(receiver) #多人收件

# 直接读取了附件的内容,为后续正文使用做准备
f = open("reportresult.html",encoding="utf-8")
mail_body = f.read()
f.close()

# 添加附件，把测试报告的html作为附件添加到邮件里
att = MIMEText(mail_body,"base64","utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment;filename = "reportresult.html"'
msg.attach(att)

# 把读取出来的附件的内容作为正文展示在邮件里
body = MIMEText(mail_body,'html','utf-8')
msg.attach(body)

# 写信发信的流程
smtp = smtplib.SMTP()    #这两行是非ssl加密的邮箱，直接登录
smtp.connect(smtpserver)  #这两行是非ssl加密的邮箱，直接登录
smtp.login(sender,pwd)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
