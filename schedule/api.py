#!/python/bin/python2.7
# -*- coding: utf-8 -*-

try:
    from xml.etree import ElementTree
except ImportError:
    from elementtree import ElementTree
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom
import getopt
import sys
import string
import time

import urllib,urllib2,cookielib
import re
import sys
import getpass
from bs4 import BeautifulSoup

import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

class CalendarList:
    def __init__(self, email, password):
        # email is the google account 
        self.cal_client = gdata.calendar.client.CalendarClient(source='qdushedule')
        self.cal_client.ClientLogin(email, password, self.cal_client.source)
        print 'Google Login Sucess!'

    def _InsertCalendar(self, title='QDU-Schedule', description='A Schedule', time_zone='Asia/Chongqing', hidden=False, location='' ,color='#2952A3'):

        calendar = gdata.calendar.data.CalendarEntry()
        calendar.title = atom.data.Title(text=title)
        calendar.summary = atom.data.Summary(text=description)
        calendar.where.append(gdata.calendar.data.CalendarWhere(value=location))
        calendar.color = gdata.calendar.data.ColorProperty(value=color)
        calendar.timezone = gdata.calendar.data.TimeZoneProperty(value=time_zone)
        
        new_calendar = self.cal_client.InsertCalendar(new_calendar=calendar)

        print 'Create Calendar Sucess!'
        return new_calendar
        

    def _InsertEvent(self, title='', content='', where='',start_time=None, end_time=None, recurrence_data=None):

        event = gdata.calendar.data.CalendarEventEntry()
        event.title = atom.data.Title(text=title)
        event.content = atom.data.Content(text=content)
        event.where.append(gdata.data.Where(value=where))
        
        if recurrence_data is not None:
            # Set a recurring event
            event.recurrence = gdata.data.Recurrence(text=recurrence_data)
        else:
            if start_time is None:
                # Use current time for the start_time and have the event 1 hour
                start_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z',time.gmtime())
                end_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z',time.gmtime(time.time() + 3600 ))
                event.when.append(gdata.data.When(start=start_time,end=end_time))

        new_event = self.cal_client.InsertEvent(event)
        print 'Insert a new Event named %s' % title
        print 'The content is %s' % content
        print 'The place is %s' % where
        print 'Time:'
        print start_time
        print end_time


    
username = 'qduschedule@gmail.com'
password = '19910829'

sample = CalendarList(username,password)
    
recurrence = ('DTSTART;VALUE=RDATE:20120820T182000Z\r\n'
            + 'DTEND;VALUE=RDATE:20120820T183000Z\r\n'
            + 'RRULE:FREQ=WEEKLY;BYDAY=Tu;UNTIL=20120924\r\n')

name = 'Recurrence Title'
description = 'This is a test description'
place = 'Recurrence Place'

sample._InsertEvent(title=name,content=description,where=place,recurrence_data=recurrence)

	
