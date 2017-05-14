import requests
import xlwt
import re
#import urllib

def geturl():
    info=[]
    for i in range (2):
        url = 'http://furhr.com/?page={}'.format(i)
        html=requests.get(url).content.decode('utf-8')#用.text会出现乱码 使用.content文字编程unicode不加decode会出现cannot use a string pattern on a bytes-like object报错
        #html=urllib.request.urlopen(url).read()#python3 urllib 使用 urllib.request.urlopen()打开网页 .read()读取
        content=re.findall(r'<tr><td>\d+</td><td>\d+</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>',html)
        for c in content:
            info.append(c)
    return info
def buildexcel():
    name=('银行信息.xls')
    wb=xlwt.Workbook(encoding='uft-8')#建表
    ws=wb.add_sheet('sheet1')#建sheet
    headdata=['公司名称','电话','地址']
    for column in range (3):
        ws.write(0,column,headdata[column],xlwt.easyxf('font:bold on'))#0行 column列 headdata对应数据 加粗
    index=1#从第一行开始
    for h in info:#从总数据中提取 每次提取一个银行的三条信息
        for l in range (len(h)):#对每个银行的信息抽取写入
            ws.write(index,l,h[l])
        index+=1#行数加1
    wb.save(name)
info=geturl()
buildexcel()
