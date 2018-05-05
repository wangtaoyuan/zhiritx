# encoding:utf-8
'''
Created on 2018年4月17日

@author: wangtaoyuan
'''  
    
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import panding
import ncepuWeeks
import time
from time import sleep
# my_sender='846292076@qq.com'    # 发件人邮箱账号
# my_pass = 'yyyofekxeuambcai'              # 发件人邮箱密码
# my_user='846292076@qq.com'      # 收件人邮箱账号，我这边发送给自己
# my_title='105实验室值日提醒'
# user_name='值日生'

date_now = int(time.strftime('%m', time.localtime()) + time.strftime('%d', time.localtime()))

date_workers = {423: '常雪松', 424: '李鑫', 425: '王阳', 426: '颉鑫', 427: '贾若愚', 428: '王涛渊', 502: '张旭', 503: '陈秀新', 504: '李鹏飞', 505: '王涛渊', 506: '王会月', 507: '李佳锦', 508: '郭佳兴', 509: '常雪松', 510: '李鑫', 511: '王阳', 512: '颉鑫', 513: '贾若愚', 514: '王涛渊'}
email_workers = {'常雪松': '626267475@qq.com', '李鑫': '907035184@qq.com',  '王阳': '28700776@qq.com',
                 '颉鑫': '837207831@qq.com', '贾若愚': '672401341@qq.com',  '王涛渊': '846292076@qq.com',
                 '李鹏飞': '1751409741@qq.com', '李佳锦': '972526556@qq.com', '王会月': '1174361204@qq.com',
                 '高靖智': '624823065@qq.com',  '张旭': '664313276@qq.com', '陈秀新': '1665150972@qq.com',
                 '郭佳兴': '1141958382@qq.com'}


i = date_now
flag = 0

line1 = """<p>莫忘值日A105</p>"""
line2 = """<a href="https://aiqi-oss1.oss-cn-beijing.aliyuncs.com/%E5%9B%BE%E7%89%87/%E5%80%BC%E6%97%A5%E8%A1%A8.png?x-oss-process=style/1">值日表</a>"""
line3 = """<p>本周为华电第%d周</p>""" % ncepuWeeks.weeks_answer
def mail(worker_name, worker_email):
        ret = True
        try:
            msg=MIMEText(line1 + line2 + line3, 'html', 'utf-8')
            msg['From']=formataddr(["提醒助理", panding.my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To']=formataddr(["勤劳的"+worker_name, worker_email])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = panding.my_title               # 邮件的主题，也可以说是标题
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，qq邮箱端口是465
            server.login(panding.my_sender, panding.my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(panding.my_sender, [worker_email, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        return ret
while(True):    
    if date_now in date_workers:
        worker_name = date_workers[date_now]
        worker_email = email_workers[worker_name]
        if flag == 0 and time.strftime('%H',time.localtime()) == '20': #九点发送信息
            ret = mail(worker_name, worker_email)#发送邮件
            if ret:
                flag = 1
                print("邮件发送成功", worker_name, worker_email)
            else:
                print("邮件发送失败")
        elif flag == 0:
            print("未到发送时间")
        else:
            print("今日已发送")
        
    else:
        print('今日不值班')
    
    date_now = int(time.strftime('%m',time.localtime()) + time.strftime('%d',time.localtime()))
    if(date_now != i and flag == 1): #只要i ！= date_now，就让flag变为0
        flag = 0#只要flag变为0，就让i = date_now
        i = date_now
        print(date_now)
     
    sleep(60)