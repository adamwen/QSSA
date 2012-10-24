#!/usr/bin/python

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

class CalendarList:

    def __init__(self, email, password):
        self.cal_client = gdata.calendar.client.CalendarClient(source='qdushedule')
        self.cal_client.ClientLogin(email, password, self.cal_client.source)

    def _InsertCalendar(self, title='QDU-Schedule', description='A Schedule', time_zone='Asia/Chongqing', hidden=False, location='' ,color='#2952A3'):
        print 'Creating new calendar with tietle %s' % title

        calendar = gdata.calendar.data.CalendarEntry()
        calendar.title = atom.data.Title(text=title)
        calendar.summary = atom.data.Summary(text=description)
        calendar.where.append(gdata.calendar.data.CalendarWhere(value=location))
        calendar.color = gdata.calendar.data.ColorProperty(value=color)
        calendar.timezone = gdata.calendar.data.TimeZoneProperty(value=time_zone)
        
        new_calendar = self.cal_client.InsertCalendar(new_calendar=calendar)

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
                end_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z',time.gmtime() + 3600)

        event.when.append(gdata.data.When(start=start_time,end=end_time))

        new_event = self.cal_client.InsertEvent(event)

if __name__=='__main__':
    email = 'qduschedule@gmail.com'
    password = '19910829'

    
    sample = CalendarList(email, password)

    lstart = time.strftime('%Y-%m-%dT%H:%M:%S.000Z',time.gmtime())
    lend   = time.strftime('%Y-%m-%dT%H:%M:%S.000Z',time.gmtime() + 3600)

    sample._InsertCalendar(title='event1',description='event1 description', where='event1 place',start_time=lstart,end_time=lend)

    print 'done'

    
