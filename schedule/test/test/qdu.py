#!/python/bin/python2.7
# -*- coding: utf-8 -*-

import time
from datetime import datetime, timedelta

import urllib,urllib2,cookielib
import re
import sys
import getpass
from bs4 import BeautifulSoup

from jw import ClassInfo
from gCalendar import CalendarList


import sys 
reload(sys) 
sys.setdefaultencoding('utf8')


def recurrence_data_processor(info):
    opening_day = datetime(2012, 9, 3)

    recurrence_type = info['rrType']
    if recurrence_type == 'single' or recurrence_type == 'double':
        interval = 'INTERVAL=2;'
    else:
        interval = ''

    start_week = info['startWeek']
    end_week = info['endWeek']

    day_type = info['day']
    
    start_day = info['nday'] - 1 + (start_week - 1) * 7

    if recurrence_type=='double' and start_week % 2 == 1:
        start_day += 7


    start_day = opening_day + timedelta(days=start_day)

    date_format = '%Y%m%d' 

    until_day = end_week * 7 + info['nday'] - 1
    until_day = opening_day + timedelta(days=until_day)
    until_day = time.strftime(date_format,until_day.timetuple())


    start_time = time.strftime(date_format,start_day.timetuple()) + 'T' + info['startTime'] 
    end_time   = time.strftime(date_format,start_day.timetuple()) + 'T' + info['endTime']  

    r1 = 'DTSTART;VALUE=RDATE:%s\r\n' % start_time
    r2 = 'DTEND;VALUE=RDATE:%s\r\n' % end_time
    r3 = 'RRULE:FREQ=WEEKLY;BYDAY=%s;%sUNTIL=%s\r\n' % (day_type,interval,until_day)
    recurrence = (r1 + r2 + r3 )
	
    return recurrence



    
	
cookie = cookielib.CookieJar()
cookieProc = urllib2.HTTPCookieProcessor(cookie)
enable_proxy = True #enable the proxy mode
proxy_handler = urllib2.ProxyHandler({'http': 'http://184.82.244.128:21'})

opener = urllib2.build_opener(cookieProc,proxy_handler)
urllib2.install_opener(opener)




schoolId = raw_input("Please input your School ID:")
pw = getpass.getpass("Please input your password:") 

email = raw_input("Please input your gmail account:")
password = getpass.getpass("Please input your password:")





url = 'http://jw.qdu.edu.cn/academic/j_acegi_security_check?j_username='+schoolId+'&j_password='+pw+'&username=&password=&login=%E7%99%BB%E5%BD%95'
response = urllib2.urlopen(url)
htmlCode = urllib2.urlopen('http://jw.qdu.edu.cn/academic/student/currcourse/currcourse.jsdo?year=32&term=2').read().decode('gbk').encode('UTF-8')

soup = BeautifulSoup(htmlCode) 

body = soup.find_all('tr','infolist_common')

length = len(body) - 19

classInfoList = []

sample = CalendarList(email,password)

for i in range(0,length):
    lesson = ClassInfo(body[i])
    for elem in lesson.info:
        recurrence = recurrence_data_processor(elem)
        lesson_title = lesson.get_name()
        teacher = '任课教师:' + lesson.get_teacher()
        place = elem['place']
        sample._InsertEvent(title=lesson_title,content=teacher,where=place,recurrence_data=recurrence)

