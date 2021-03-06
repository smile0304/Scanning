#-*- coding:utf-8 -*-
import optparse
import urllib2
import re
import os
import urlparse
import writefile
import time
from urllib2 import HTTPError, URLError
from httplib import responses
from writefile import writefile
from logging import thread
from multiprocessing import Pool
from _ctypes_test import func
houtai = []
threads=[]
list = []
list403=[]
result_list=[]
Msgnum = 0 #判断错误次数
author= u"""
     "anuthor: smile.苦笑"
     "email:tsmielt@gmail.com"
     """
def judlist(result_list,list403):
    if len(result_list) or len(list403):
        print u"已找到地址:"
        for i in range(len(list403)):
            print "\t"+list403[i]
        for i in range(len(result_list)):
            print "\t"+result_list[i]
    else:
        print u"没有找到存在的地址"
        exit(0)
def testbackground():
    print u"可能为后台的地址"
    for i in range(len(houtai)):
        print '\t'+houtai[i]
def urlHandling(url):
    if not re.match(r'^http:/{2}\w.+$',url):
        name = url
        url = "http://"+url
    else:
        url = urlparse.urlparse(url).netloc
        name = url
        url = "http://"+url
    return name,url
def run(dici,stime):
    global list403
    u"""判断http请求码"""
    try:
        status = urllib2.urlopen(dici,timeout=10).getcode()
        if status == 200:
            print dici
            time.sleep(stime)
            return dici
        else:
            print dici
            time.sleep(stime)
    except HTTPError as e:
        if e.code==403:
            print dici
            list403.append(dici)
            time.sleep(stime)
        else:
            print dici
            time.sleep(stime)
    except URLError as e:
        print u"连接超时:" + dici
def getkeyword(url):
    u"""判断请求后台页面的关键字"""
    keyword = u"用户名|邮箱|密码|username|user|pass|password|admin|login|登陆|验证码|管理|user_login"
    try:
        response = urllib2.urlopen(url)
        html = response.read()
    except URLError as e:
        pass
    except HTTPError as e:
        pass
    keywordlist = re.findall(keyword, html)
    if len(keywordlist):
        houtai.append(url)
    else:
        return
def readdic(filename,url):
    u"""读取字典文件，进行字符串拼接"""
    try:
        f = open(filename,'r')
    except IOError as e:
        print u"%s不存在,请检查文件名" % (filename)
        exit(0)
    dic1 = []
    dic2 = []
    while True:
        line = f.readline()
        if line:
            line = line.strip('')
            dic1.append(line)
        else:
            break
    f.close()
    for i in range(len(dic1)):
        str = dic1[i]
        if str.startswith('/'):
            url1 = url + str
            dic2.append(url1)
        else:
            url1 = url + "/" + str
            dic2.append(url1)
    return dic2
def main():
    print author
    parser = optparse.OptionParser(u'输入格式: -u "url" [-T] "进程数(默认为5，建议不要超过20)" [-f] "字典文件(可选)" [-t] "间隔时间"')
    parser.add_option('-u','--url',dest='url',type='string',help=u'输入url地址')
    parser.add_option('-f','--file',dest='filename',type="string",help=u'请输入字典文件名')
    parser.add_option('-T',dest='threadnum',type='int',help=u'输入进程数量,默认为5')
    parser.add_option('-t',dest='stime',type='int',help=u'间隔时间,默认为0')
    (options,args) = parser.parse_args()
    url = options.url
    filename = options.filename
    threadnum = options.threadnum
    stime = options.stime
    if url == None:
       print parser.usage
       exit(0)
    if filename == None:
        filename="all.txt"
    if threadnum == None:
        threadnum = 5
    if stime == None:
        stime = 0
    name,url = urlHandling(url)
    dic = readdic(filename,url)
    pool = Pool(threadnum)
    for i in range(len(dic)):
        res = pool.apply_async(func=run,args=(dic[i],stime))
        list.append(res)
    pool.close()
    pool.join()
    for res in list:
        if res.get() == None:
            pass
        else:
            result_list.append(res.get())
    judlist(result_list,list403)
    for i in range(len(result_list)):
        getkeyword(result_list[i])
    #检测关键字字段判断可能为后台的地址
    if len(houtai):
        testbackground()
    else:
        print u"爬虫没有判断出可能为后台的地址，请手动确认!"
    writefile(name,houtai,result_list,list403)
    print u'已在当前文件夹下生成%s.txt的扫描结果' % (name)
    
if __name__ == '__main__':
    main()