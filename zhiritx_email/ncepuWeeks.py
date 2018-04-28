# encoding:utf-8
'''
Created on 2018年3月12日

@author: wangtaoyuan
'''
import time
# encoding=utf-8
# sd = 5
# sm = 3
# sy = 2018

#输入当前日期
date = time.strftime('%Y%m%d')
strdate = '当前时间：' + time.strftime('%Y')+'年' + time.strftime('%m')+'月' + time.strftime('%d')+'日' + time.strftime('%H:%M:%S')
print (strdate)

weeks_answer = 0

# date = input("请输入6位年月日")
ny = int(date[0: 4])
nm = int(date[4: 6])
nd = int(date[6: 8])

#设置学期的第一天
startd = '20180305'
sy = int(startd[0: 4])
sm = int(startd[4: 6])
sd = int(startd[6: 8])

# print (nd, "-", sd, '=', nd - sd)
#做差
cy = ny - sy
cm = nm - sm
# print (cm)
cd = nd - sd

days = 0#设置天数变量


def RunYN(y):
    if y % 100 == 0:
        if y % 400 == 0:
            return 0
        else:
            return 1
    elif y % 4 == 0:
        return 0
    else:
        return 1

def ReMoDays(y, m ,d):
    RMDays = 0
    if m == 2:
        if RunYN(y) == 0:
            RMDays = 29 - d
        else:
            RMDays = 28 - d
    elif m in (1, 3, 5, 7, 8, 10, 12):
        RMDays = 31 -d
    else:
        RMDays = 30 - d   
    return RMDays + 1

def AllMoDays(m, y):
    AMDays = 0
    if m == 2:
        if RunYN(y) == 0:
            AMDays = 29
        else:
            AMDays = 28
    elif m in (1, 3, 5, 7, 8, 10, 12):
        AMDays = 31
    else:
        AMDays = 30   
    return AMDays

def ReYeDays(y, m ,d):
    RYDays = ReMoDays(y, m, d)#第一个月剩余天数
    for i in range(m+1, 13):
        RYDays = RYDays + AllMoDays(i, y)
    return RYDays


def PaYeDays(y, m, d):
    PYDays = 0
    for i in range(1, m):
        PYDays = PYDays + AllMoDays(i, y)
    PYDays = PYDays + d
    return PYDays





def AllYeDays(y):
    if RunYN(y) == 0:
        return 366
    else:
        return 365
    
   



#1.先于开始年 2.后于开始年 3.同年
if cy < 0:
    print ('error year')
elif cy > 0:
    i = cy
    y = sy
    while(i > -1):
        i = i - 1
        if y == sy:
            #开始年，计算当年剩下的天数
            days = days + ReYeDays(sy, sm, sd)
            print ('当年剩下天数', days)
        elif y == ny:
            #本年，计算当年过去的天数
            days = days + PaYeDays(ny, nm ,nd)
        else:
            #中间年，计算全年天数
            days = days + AllYeDays(y)
        y = y + 1#计算完后增加到下一年下一个while循环
else:#同年又分为1.先于开始月2.后于开始月3.同月
    if cm < 0:
        print ('error moon')
    elif cm > 0:#不同月
        i = cm
        m = sm
        while(i > -1):
            
            if m == sm:
                # 开始月，计算当月剩下的天数
                days = days + ReMoDays(sy, sm, sd)
                # print ('开始月天数', days)
            elif m == nm:
                # 本月，计算当月过去的天数
                days = days + nd
                # print ('本月', days)
            else:
                # 中间月，计算全月天数
                days = days + AllMoDays(m, ny)
            m = m + 1  # 计算完后增加到下一月下一个while循环
            i = i - 1
    else:#同月
        days = nd - sd + 1
        
# print (days)

if days % 7 == 0:
	weeks_answer = days // 7
else:
	weeks_answer = days //7 + 1
	
if __name__ == "__main__":  
	print ('第', weeks_answer , '周')
	strnweeks = '第' + str(weeks_answer) + '周'  
# f = open('weeks.txt', 'w')
# f.write(strdate)
# f.write('\n')
# f.write(strnweeks)
# f.close
#弹出windows提示窗口
# import win32api,win32con  
# win32api.MessageBox(0, strdate, strnweeks,win32con.MB_OK) 
