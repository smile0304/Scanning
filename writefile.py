#-*- coding:utf-8 -*-
def writefile(filename,houtai,list):
    text= """
---------------------------------------扫描结果-------------------------------------
------------------------------------------------------------------------------------
    |    |    |    |    |    |    |    |    |    |    |    |    |
    |    |    |    |    |    |    |    |    |    |    |    |    |
    |    |    |    |    |    Author:smile.苦笑             |    |
    |    |    |    |    |  E-mail:smile@smilehacer.net     |    |
    |    |    |    |    |    |    |    |    |    |    |    |    |
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
   """
    f = open(filename+".txt",'w')
    f.write(text + "\n")
    f.write("可能为后台的目录:\n")
    for i in range(len(houtai)):
        f.write(houtai[i] + "\n")
    if len(houtai):
        f.write("扫描到的目录:\n")
        for i in range(len(list)):
            f.write(list[i]+ "\n")
    else:
        f.write("爬虫没有判断出可能的后台，请手动判断!")
    f.close()