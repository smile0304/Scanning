# Scanning目录扫描

说明:
	代码默认的字典文件是 all.txt 大家可以更换这个字典文件，但是要是看不懂代码的话就知己把自己的字典文件修改成all.txt吧</br>
	也可以制定别的目录哦</br>
	
	
功能说明:
		可以扫描网站的目录，但是只会保留返回403跟200的页面
		但是403多半没什么用= =！
		有爬虫可以去爬可能是后台的页面,本程序的关键字有:用户名|邮箱|密码|username|user|pass|password|admin|login|登陆|验证码|管理|user_login
		误报的情况肯定有了  比如说wordpress几乎只要存在的页面都有登陆等字样
		
待处理：自定义404页面，以及403页面的显示
		
重要说明:字典中请不要出现空行，如果出现程序将会报错</br>

使用方法:
Usage: 输入格式: -u "url" [-T] "进程数[可选](默认为5)" [-f] "字典文件(可选，默认为all.txt) [-t] "线程休眠时间(可选，默认为0)""</br>

Options:


  -h, --help            show this help message and exit
  -u URL, --url=URL     输入url地址
  -f FILENAME, --file=FILENAME
                        请输入字典文件名
  -T THREADNUM          输入进程数量,默认为5
  -t STIME              间隔时间,默认为0 (考虑防火墙)
 
 
例如：  
	
		scanning.py -u "xxxxxxx.com"

		scanning.py -u "xxxxxxx.com" -f "1.dic"
		
		scanning.py -u "xxxxxxx.com" -f "1.dic" -T "20"
		
		scanning.py -u "xxxxxxx.com" -f "1.dic" -T "20" -t "3"

tsmilet@gmail.com