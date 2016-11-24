#-*- coding:utf-8 -*-
import re
import urllib2
import urlparse
import socket
from urlparse import *
"""将url转化为ip"""
def ipTransformation(url):
    if not re.match(r'^http:/{2}\w.+$',url):
        ip = socket.gethostbyname(url)
    else:
        url = urlparse(url).netloc
        ip = socket.gethostbyname(url)
    return ip
"""查询旁站"""
def NextStation(ip):
    url = urllib2.urlopen('http://www.bing.com/search?q=ip:'+ip+'&count=50')
    html = url.read()
    match = re.findall(r'<li class=\"b_algo\"><h2><a target=\"_blank\" href=\"(.*?)\"', html)
    match1 = re.findall(r'<li class=\"b_algo\"><div class=\"b_title\"><h2><a target=\"_blank\" href=\"(.*?)\"', html)
    match = match + match1
    return match

"""打印所有存在的旁站,并将输出格式进行处理"""
def printNextStation(match):
    if match:
        print u"一共存在%s个旁站" % (len(match))
        for i in range(len(match)):
            url = match[i]
            r = urlparse(url).netloc
            print "%s" % r
    else:
        print u"没有跟该网站同IP的域名"
"""
ip=ipTransformation(url)
match = NextStation(ip)
printNextStation(match)
"""
