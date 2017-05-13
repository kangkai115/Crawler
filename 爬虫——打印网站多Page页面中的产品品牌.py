# _*_coding:utf-8_*_
#打印网站多Page页面中的产品品牌
import re
import requests
# import importlib,sys      python2中用的 3已弃用
# importlib.reload(sys)
# sys.setdefaultencoding('utf-8')

url='https://www.crowdfunder.com/?page='
for i in range(3):#3页内容
	html=requests.get(url+'%d'%i).text #此处.text后面就html 否则下一行需要html.text
	name_url=re.findall('<div class="card-title">(.*?)</div>',html)
	f=open('d:\\11.txt','w')
	for each in name_url:
		f.write(each+'\n')
	f.close()
	# 	print(each+'\n') #每提取一个换一行
	# print(len(name_url))#打印此页有多少个品牌

# f=open('d:\\b.txt','w')
# for each in html.text:
# 	f.write(each)
# f.close()

###!!!未解决问题：第4页有个 'gbk' codec can't encode character '\u2122' in position 9: illegal multibyte sequence错误