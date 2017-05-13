# -*- coding:utf-8 -*-
import requests
import re
def getpartUrl(url):
    html_all=requests.get(url).text
    html_block=re.findall(r'<div class="box-hd"><h3 class="box-t-l">北京历史天气详情</h3></div>(.*?)</div>',html_all,re.S)
    html=re.findall(r'<a href="(.*?)">',str(html_block),re.S)
    return html
def
url='http://lishi.tianqi.com/beijing/index.html'
url_detail=getpartUrl(url)