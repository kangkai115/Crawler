import requests,re,xlwt
from bs4 import BeautifulSoup



def getcontent(url):
    html=requests.get(url).content.decode('utf-8')#用.text也行
    bs = BeautifulSoup(html,'html.parser')
    bs = str(bs.select('div[class="article block untagged mb15"]'))#查找符合select内容的并转化成字符串，下一行分块
    #bs = str(bs.find_all('div',class_="article block untagged mb15")[0])
    bs = bs.split('<div class="article block untagged mb15"')#利用分列拆快， 每块包含昵称 点赞数 内容
    bs=bs[1:]#第一个元素是‘[’可以去掉
    page_all=[]
    for b in bs:#把每块循环处理
        name = re.findall(r'<h2>(.*?)</h2>',b)#昵称用h2
        content=re.findall(r'<span>(.*?)</span>',b)#content大多在span
        content=content[-1:]#匿名用户也有span行 内容在最后一个content
        #content=list(content[0].replace('<br/>',''))#删除正文中的<br/>
        support=re.findall(r'<span class="stats-vote"><i class="number">(.*?)</i> 好笑</span>',b)
        # support=support[0].replace('<br/>','')#删除正文中的<br/>
        # print(content)
        name.extend(support)#把name content support合并成list中的一项
        name.extend(content)#把name content support合并成list中的一项
        page_all.append(name)#加到网页汇总列表中
    page_all=page_all[1:]
    return page_all

def write_excel(web_all):
    name=('糗百.xls')
    wb=xlwt.Workbook(encoding='utf-8')#建工作簿
    ws=wb.add_sheet('sheet1')#建sheet页
    headdata=['昵称','点赞数','内容']#建title
    for column in range (3):
        ws.write(0,column,headdata[column],xlwt.easyxf('font:bold on'))#写title
    index=1#列数，for中会+1
    for h in web_all:
        for l in range (len(h)):
            ws.write(index,l,h[l])#循环写入
        index+=1
    wb.save(name)


url='http://www.qiushibaike.com/textnew/page/%d/?s=4983129'
web_all=[]
for i in range (1,3):
    page_all=getcontent(url%i)
    for pa in page_all:#讲每一页的page_all汇总到web_all中
        web_all.append(pa)
write_excel(web_all)



