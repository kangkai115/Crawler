# -*- coding:utf-8 -*-
from lxml import etree
import requests
import re


def getHtml(url):#获取主页的html内容
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
    html=requests.get(url,headers=header )
    return html.text

def getUrl(html_text):#获取跳转页的数字号
    html_numberpart=re.findall(r'<a href="/story/(.*?)" class',html_text,re.S)
    return html_numberpart

def getContent(number):#爬跳转页内容
    url='http://daily.zhihu.com/story/'+str(number)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
    html = requests.get(url, headers=header).text
    title=re.findall(r'<h1 class="headline-title">(.*?)</h1>',html,re.S)#爬标题
    content=re.findall(r'<p>(.*?)</p>',html,re.S)#爬内容
    # selector=etree.HTML(html)
    # content=selector.xpath('/div/text()')
    # print(content)
    # for each in content:
    #     print(each)
    return (title,content)

url='http://daily.zhihu.com'
f=open('e:\\1.txt','w',encoding='utf-8')#不写encoding='utf-8'会出现 'gbk' codec can't encode character xxx....的问题
for number in getUrl(getHtml(url)):
    tilte_and_content=getContent(number) #标题加内容
    for details in tilte_and_content:
        for details1 in details:
            f.write(details1+'\n')
    f.write('\n\n\n')
    # print(tilte_and_content[0],'\n',tilte_and_content[1])
f.close()

