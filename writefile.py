#-*- coding:utf-8 -*-
def writefile(filename,houtai,result_list,list403):
    text= """
---------------------------------------扫描结果-------------------------------------
------------------------------------------------------------------------------------
    |    |    |    |    |    |    |    |    |    |    |    |    |
    |    |    |    |    |    |    |    |    |    |    |    |    |
    |    |    |    |    |    Author:smile.苦笑   |    |    |    |
    |    |    |    |    |  E-mail:smile@smilehacer.net|    |    |
    |    |    |    |    |    |    |    |    |    |    |    |    |
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
   """
    f = open(filename+".txt",'w')
    f.write(text + "\n")
    f.write("可能为后台的目录:\n")
    for i in range(len(houtai)):
        f.write(houtai[i])
    if len(houtai):
        f.write("扫描到的目录:\n")
        for i in range(len(result_list)):
            f.write(result_list[i])
        for i in range(len(list403)):
            f.write(list403[i])
    else:
        f.write("爬虫没有判断出可能的后台，请手动判断!")
    f.close()