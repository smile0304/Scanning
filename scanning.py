#-*- coding:utf-8 -*-
import optparse
import urllib2
import re
import os
import urlparse
import writefile
from color import Color
from urllib2 import HTTPError, URLError
from httplib import responses
from writefile import writefile
clr = Color()
houtai = []
Msgnum = 0 #判断错误次数
author= u"""
             へ　　　　　／|
　　/＼7　　　 ∠＿/
　 /　│　　 ／　／
　│　Z ＿,＜　／　　 /`ヽ
　│　　　　　ヽ　　 /　　〉
　 Y　　　　　`　 /　　/
　●　　●　　〈　　/
　()　 へ　　　　|　＼〈
　　> _　 ィ　 │ ／／
　 / へ　　 /　＜| ＼＼
　 ヽ_　　(_／　 │／／
　　7　　　　　　　|／
　　＞―r￣￣`―＿

    
     "******************************************"
     "anuthor: smile.苦笑"
     "email:smile@smilehacker.net"
     "当眼泪流尽的时候，留下的应该是坚强"
     """
def testbackground():
    clr.print_blue_text(u"可能为后台的地址")
    for i in range(len(houtai)):
        clr.print_green_text('\t'+houtai[i])
def urlHandling(url):
    if not re.match(r'^http:/{2}\w.+$',url):
        name = url
        url = "http://"+url
    else:
        url = urlparse.urlparse(url).netloc
        name = url
        url = "http://"+url
    return name,url
def run(dic):
    u"""判断http请求码"""
    list = []
    for i in range(len(dic)):
        try:
            status = urllib2.urlopen(dic[i],timeout=10).getcode()
            if status == 200:
                clr.print_green_text(dic[i])
                list.append(dic[i])
            else:
                clr.print_red_text(dic[i])
        except HTTPError as e:
            if e.code==403:
                clr.print_green_text(dic[i])
                list.append(dic[i])
            else:
                clr.print_red_text(dic[i])
        except URLError as e:
            print u"网络连接失败"
            
    if len(list):
        clr.print_blue_text(u"已找到地址:")
        for i in range(len(list)):
            clr.print_green_text("\t"+list[i])
        return list
    else:
        clr.print_red_text(u"没有找到存在的地址")
        exit(0)

def getkeyword(url):
    u"""判断请求后台页面的关键字"""
    keyword = u"用户名|邮箱|密码|username|user|pass|password|admin|login|登陆|验证码|管理|user_login"
    response = urllib2.urlopen(url)
    html = response.read()
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
            #print url
            dic2.append(url1)
        else:
            url1 = url + "/" + str
            dic2.append(url1)
    return dic2
def main():
    clr.print_green_text(author)
    parser = optparse.OptionParser(u'输入格式: -u "url" [-f] "字典文件(可选)"')
    parser.add_option('-u','--url',dest='url',type='string',help='输入url地址')
    parser.add_option('-f','--file',dest='filename',type="string",help='请输入字典文件名')
    (options,args) = parser.parse_args()
    url = options.url
    filename = options.filename
    if url == None:
        clr.print_blue_text(parser.usage)
        exit(0)
    if filename == None:
        #filename = "dic/all.txt"
        filename="all.txt"
    name,url = urlHandling(url)
    dic = readdic(filename,url)
    print dic
    list = run(dic)
    for i in range(len(list)):
        getkeyword(list[i])
    #检测关键字字段判断可能为后台的地址
    if len(houtai):
        testbackground()
    else:
        print u"爬虫没有判断出可能为后台的地址，请手动确认!"
    writefile(name,houtai,list)
    print u'已在当前文件夹下生成%s.txt的扫描结果' % (name)
if __name__ == '__main__':
    main()