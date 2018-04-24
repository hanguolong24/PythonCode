#!/usr/bin/env python
#-*-coding:utf-8 -*-
#Time:2018/4/23  17:06
#Author:Kevin Hon
#--------------------------------------------------

'''这段代码是用来实现SSL加密方式发送带附件测试报告的邮件的功能'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 定义发邮件的各类基础参数
smtpserver = "smtp.qq.com"
port = 465
sender = "858198672@qq.com"
pwd ="acucmzogypngbdeh"  # QQ邮箱配置的授权码，用来登录，不是密码，但是是代替密码的功能
receiver = "185983895@qq.com"  # 单个收件人
# receiver = ["185983895@qq.com","hanguolong21@163.com"]  #多个收件人

# 带正文的写信的模板，无附件，最基本的模板格式
# subject = "这是一封测试邮件"
# # body = '<pre><h1>测试报告邮件</h1></pre>'
# with open("E:\\Practice\\model\\reportresult.html",encoding="utf-8") as f:
#     body = f.read()
# msg = MIMEText(body,'html','utf-8')
# msg['from'] = sender
# msg['to'] = receiver
# msg['subject'] = subject

# 带附件的写信模板
msg = MIMEMultipart()
msg['Subject'] = '今天韦少会去防守卢比奥？'
msg['From'] = sender
msg['To'] = receiver    #单人收件
# msg['To'] = "；".join(receiver) #多人收件

# 直接读取了附件的内容
f = open("reportresult.html",encoding="utf-8")
mail_body = f.read()
f.close()

# 添加附件
att = MIMEText(mail_body,"base64","utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment;filename = "reportresult.html"'
msg.attach(att)

# 把读取出来的附件的内容作为正文展示在邮件里
body = MIMEText(mail_body,'html','utf-8')
msg.attach(body)


# 写信发信的流程
# smtp = smtplib.SMTP()    #这两行是非ssl加密的邮箱，直接登录
# smtp.connect(smtpserver)  #这两行是非ssl加密的邮箱，直接登录
smtp = smtplib.SMTP_SSL(smtpserver,port)   #这行是ssl方式登录邮箱，QQ邮箱用的是这种方式
smtp.login(sender,pwd)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
