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
from datebase import select_zrtx


date_now = int(time.strftime('%m', time.localtime()) + time.strftime('%d', time.localtime()))  # 月和日,例如601->6月1号
i = date_now
flag = 0
line1 = """<p>莫忘值日A105</p>"""
line2 = """<a href="https://aiqi-oss1.oss-cn-beijing.aliyuncs.com/%E5%9B%BE%E7%89%87/%E5%80%BC%E6%97%A5%E8%A1%A8.png?x-oss-process=style/1">值日表</a>"""


# print('邮件内容：%s\n%s\n%s' % (line1, line2, line3))
def mail(worker_name, worker_email):
        ret = True
        try:
            global line3
            msg=MIMEText(line1 + line2 + line3, 'html', 'utf-8')
            msg['From'] = formataddr(["提醒助理", panding.my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["勤劳的"+worker_name, worker_email])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = panding.my_title               # 邮件的主题，也可以说是标题
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，qq邮箱端口是465
            server.login(panding.my_sender, panding.my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(panding.my_sender, [worker_email, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        return ret


while(True):
    if(date_now != i and flag == 1):  # 只要i ！= date_now，就让flag变为0
        flag = 0 #只要flag变为0，就让i = date_now
        i = date_now
        print(date_now)

    global line3
    print(time.strftime('%Y年%m月%d日'))
    line3 = """<p>本周为华电第%d周</p>""" % ncepuWeeks.weeks(time.strftime('%Y%m%d'))
    print(line3)

    # if date_now in date_workers:
    if select_zrtx("select name from date_work where date=%d" % date_now) != -1:
        # worker_name = date_workers[date_now]
        worker_name = select_zrtx("select name from date_work where date=%d" % date_now)
        # worker_email = email_workers[worker_name]
        worker_email = select_zrtx("select email from worker where name='%s'" % worker_name)
        print('值日生是:%s, 邮箱为:%s' % (worker_name, worker_email))
        if flag == 0 and time.strftime('%H',time.localtime()) == '09':  # 九点发送信息
            ret = mail(worker_name, worker_email)  # 发送邮件
            if ret:
                flag = 1
                i = date_now
                print("邮件发送成功", worker_name, worker_email)
            else:
                print("邮件发送失败")
        elif flag == 0:
            print("未到发送时间")
        else:
            print("今日已发送")
        
    else:
        print('今日无人值日')
    
    date_now = int(time.strftime('%m', time.localtime()) + time.strftime('%d', time.localtime()))
     
    sleep(300)
