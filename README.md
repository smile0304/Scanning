# Scanning目录扫描

说明:此代码就是自己无聊随便写的，大家有什么意见或者建议可以给我提，让我学习学习，大家一起进步</br>

	
	代码默认的字典文件是 all.txt 大家可以更换这个字典文件，但是要是看不懂代码的话就知己把自己的字典文件修改成all.txt吧</br>
	也可以制定别的目录哦</br>
	
	因为python的多线程比较废，单线程比多线程都快，所以本程序采用了多进程</br>
	
功能说明:可以扫描网站的目录，但是只会保留返回403跟200的页面</br>
		但是403多半没什么用= =！ </br>
		有爬虫可以去爬可能是后台的页面,本程序的关键字有:用户名|邮箱|密码|username|user|pass|password|admin|login|登陆|验证码|管理|user_login</br>
		误报的情况肯定有了  比如说wordpress几乎只要存在的页面都有登陆等字样</br>

使用方法:
Usage: 输入格式: -u "url" [-T] "进程数(默认为5，建议不要超过20)" [-f] "字典文件(可选)"</br>

Options:</br>
  -h, --help            show this help message and exit</br>
  -u URL, --url=URL     输入url地址</br>
  -f FILENAME, --file=FILENAME</br>
                        请输入字典文件名</br>
  -T THREADNUM          输入进程数量,默认为5</br>
 
 
例如：  scanning.py -u "xxxxxxx.com"</br>

		scanning.py -u "xxxxxxx.com" -f "1.dic"</br>
		
		scanning.py -u "xxxxxxx.com" -f "1.dic" -T "20"</br>
		
联系方式:smile@smilehakcer.net