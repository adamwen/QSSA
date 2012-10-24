#!/python/bin/python2.7
# -*- coding: utf-8 -*-
import urllib,urllib2,cookielib
import re
import sys
from bs4 import BeautifulSoup


cookie = cookielib.CookieJar()
cookieProc = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(cookieProc)

urllib2.install_opener(opener)


url = 'http://www.sina.com.cn'

response = urllib2.urlopen(url)

body = urllib2.urlopen(url)

html = body.read()
html = html.decode('gbk')
html = html.encode('utf-8')
#html = re.sub('charset=gb2312','charset=utf-8',html);

soup = BeautifulSoup(html)

print soup.prittify()

