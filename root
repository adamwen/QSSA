#!/python/bin/python2.7
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

class ClassInfo(object):
    """ a class to save the class info"""

    def __init__(self,html):
        self.number = ''  #The Lesson's num;PY:KeChengHao 
        self.order = ''   #The Lesson's order num;PT:KeXuHao	
        self.name = ''    #The Lesson's name
        self.teacher = '' #The Lesson's Teacher 
        self.credit = ''  #The Lesson's credit;PY:XueFen
        self.type1 = ''   #The Lesson's type;PY:XuanKeShuXing
        self.type2 = ''   #The Lesson's type;PY:KaoHeFangShi
        self.examtype = ''#The Lesson's exam type

        self.info = []


        #the length,to describe the lesson appearing times in one week
        self.length = 0

        self.set_all(html)

    
    def set_all(self,html):
        self.set_number(html)
	self.set_order(html)
	self.set_name(html)
	self.set_teacher(html)
	self.set_credit(html)
	self.set_type1(html)
	self.set_examtype(html)
	self.set_type2(html)
	self.set_info(html)
	

    def set_number(self,html):
        #set the lesson number
	self.number = html.contents[1].string.strip().encode('utf-8')

    def get_number(self): 
        return self.number
	
    def set_order(self,html):
        #set the lesson order
        self.order = html.contents[3].string.strip().encode('utf-8')

    def get_order(self):
        return self.order

    
    def set_name(self,html):
        #set the lesson title
        self.name = html.contents[5].a.string.strip().encode('utf-8')
	
    def get_name(self):
        return self.name

    def set_teacher(self,html):
        #set the lesson's teacher
        self.teacher = html.contents[7].a.string.strip().encode('utf-8')

    def get_teacher(self):
        return self.teacher

    def set_credit(self,html):
        #set the lesson's teacher
        self.credit = html.contents[9].string.strip().encode('utf-8')

    def get_credit(self):
        return self.credit

    def set_type1(self,html):
        self.type1 = html.contents[11].string.strip().encode('utf-8')
	
    def get_type1(self):
        return self.type1

    def set_type2(self,html):
        self.type2 = html.contents[13].string.strip().encode('utf-8')

    def get_type2(self):
        return self.type2

    def set_examtype(self,html):
        self.examtype = html.contents[15].string.strip().encode('utf-8')

    def get_examtype(self):
        return self.examtype

    def set_info(self,html):
        #set the lesson's rest info:recurring type,startweek,endweek,day,place,starttime,endtime

        startTimeDict = {'1': '000000',
                         '2': '010000',
                         '3': '021000',
                         '4': '031000',
                         '5': '053000',
                         '6': '063000',
                         '7': '073000',
                         '8': '083000',
                         '9': '103000',
                         '10':'113000',
                         '11':'123000'}


        endTimeDict = {'1': '005000',
                       '2': '015000',
                       '3': '030000',
                       '4': '040000',
                       '5': '062000',
                       '6': '072000',
                       '7': '082000',
                       '8': '092000',
                       '9': '112000',
                       '10':'122000',
                       '11':'135000'}

        table = html.contents[19].table.contents
        length =  len(table)

        for i in range(1,length,2):
            """the following is to process and get the recurrence type,start week,end week"""

            infoDict = {}
            oweek = table[i].contents[1].string.strip().encode('utf-8')
            weekList = []

            if ',' in oweek:
                weekList = oweek.split(',')
            else:
                weekList.append(oweek)

            for week in weekList:
                weekLen = len(week)
                if week == '单周':
                    infoDict['rrType'] = 'single'
                    infoDict['startWeek'] = 1
                    infoDict['endWeek'] = 18
                elif week == '双周':
                    infoDict['rrType'] = 'double'
                    infoDict['startWeek'] = 1
                    infoDict['endWeek'] = 18
                elif weekLen <= 2:
                    infoDict['rrType'] = 'once'
                    infoDict['startWeek'] = int(week)
                    infoDict['endWeek'] = int(week)
                elif weekLen == 3 or weekLen <= 5 or weekLen == 4:
                    infoDict['rrType'] = 'normal'
                    temp = week.split('-')
                    infoDict['startWeek'] = int(temp[0])
                    infoDict['endWeek'] = int(temp[1])
                else:
                    if week[0:3] == '单':
                        infoDict['rrType'] = 'single'
                        temp = week[6:].split('-')
                        infoDict['startWeek'] = int(temp[0])
                        infoDict['endWeek'] = int(temp[1])
                    else: 
                        infoDict['rrType'] = 'double'
                        temp = week[6:].split('-')
                        infoDict['startWeek'] = int(temp[0])
                        infoDict['endWeek'] = int(temp[1])
                    



                dayDict = {'周日':'SU','周一':'MO','周二':'TU','周三':'WE','周四':'TH','周五':'FR','周六':'SA'}
                ndayDict = {'周日':7,'周一':1, '周二':2, '周三':3, '周四':4 ,'周五':5 ,'周六':6}
	        day = table[i].contents[3].string.strip().encode('utf-8')
                infoDict['nday'] = ndayDict[day]
                infoDict['day'] = dayDict[day] 

	        time = table[i].contents[5].string.strip().encode('utf-8')
                if '、' in time:
                    time = time.split('、')
                else:
                    if '-' in time:
                        time = time.split('-')
                infoDict['startTime'] = startTimeDict[time[0]]
                infoDict['endTime'] = endTimeDict[time[-1]]




	        place = table[i].contents[7].string.strip().encode('utf-8')

                infoDict['place'] = place
                self.info.append(infoDict.copy())

    def __del__(self):
        del self.info


