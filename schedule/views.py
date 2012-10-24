from django.template import Template, Context, RequestContext
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from schedule.models import Info
import datetime

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

def index(request):
    t = get_template('index.html')
    html = t.render(Context())
    return HttpResponse(html)

def about(request):
    t = get_template('about.html')
    html = t.render(Context())
    return HttpResponse(html)
    
@csrf_exempt
def submit(request):
    if request.method == 'POST':
        tschoolId = request.POST['schoolNum']
        tpw = request.POST['schoolpasswd']
        temail = request.POST['email']
        tpassword = request.POST['password']
        errorFlag = 0
        try:
            user = Info(schoolId=tschoolId,pw=tpw,email=temail,password=tpassword)
            user.save()
            run(tschoolId,tpw,temail,tpassword) 
        except Exception,e:
            wrongInfo = str(e)
            print wrongInfo
            errorFlag = 1
        finally:
            if errorFlag == 1:
                print wrongInfo
                if wrongInfo == 'school' :
                    ret = get_template('sloginwrong.html')
                    html = ret.render(Context())
                    return HttpResponse(html)
                else:
                    if wrongInfo == 'Incorrect username or password':
                        ret = get_template('gloginwrong.html')
                        html = ret.render(Context())
                        return HttpResponse(html)

            ret = get_template('success.html')
            html = ret.render(Context())
            return HttpResponse(html)

def gloginwrong(request):
    t = get_template('gloginwrong.html')
    html = t.render(Context())
    return HttpResponse(html)

def sloginwrong(request):
    t = get_template('sloginwrong.html')
    html = t.render(Context())
    return HttpResponse(html)




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

    until_day = end_week * 7 + info['nday'] - 2
    until_day = opening_day + timedelta(days=until_day)
    until_day = time.strftime(date_format,until_day.timetuple())


    start_time = time.strftime(date_format,start_day.timetuple()) + 'T' + info['startTime'] 
    end_time   = time.strftime(date_format,start_day.timetuple()) + 'T' + info['endTime']  

    r1 = 'DTSTART;VALUE=RDATE:%s\r\n' % start_time
    r2 = 'DTEND;VALUE=RDATE:%s\r\n' % end_time
    r3 = 'RRULE:FREQ=WEEKLY;BYDAY=%s;%sUNTIL=%s\r\n' % (day_type,interval,until_day)
    recurrence = (r1 + r2 + r3 )
	
    return recurrence


def run(schoolId,pw,email,password):
    cookie = cookielib.CookieJar()
    cookieProc = urllib2.HTTPCookieProcessor(cookie)
   

    opener = urllib2.build_opener(cookieProc)
    
    urllib2.install_opener(opener)


    pw = urllib.quote(pw)
    url = 'http://jw.qdu.edu.cn/academic/j_acegi_security_check?j_username='+schoolId+'&j_password='+pw+'&username=&password=&login=%E7%99%BB%E5%BD%95'
    response = urllib2.urlopen(url)
    htmlCode = urllib2.urlopen('http://jw.qdu.edu.cn/academic/student/currcourse/currcourse.jsdo?year=32&term=2').read().decode('gbk').encode('UTF-8')

    soup = BeautifulSoup(htmlCode) 

    body = soup.find_all('tr','infolist_common')
    length = len(body) - 19

    try:
        if length < 0:
            raise Exception('school')

        classInfoList = []
        #sample = CalendarList(email,password)
        for i in range(0,length):
            lesson = ClassInfo(body[i])
            for elem in lesson.info:
                recurrence = recurrence_data_processor(elem)
                lesson_title = lesson.get_name()
                teacher = lesson.get_teacher()
                place = elem['place']
                print lesson_title,teacher,place
                #sample._InsertEvent(title=lesson_title,content=teacher,where=place,recurrence_data=recurrence)
    except Exception,e:
        raise Exception(str(e))

