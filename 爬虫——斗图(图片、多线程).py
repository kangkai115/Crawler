import requests,threading,re
from lxml import etree
from bs4 import BeautifulSoup

def get_page_url(homepage_url):#所有连接
    page_url=[]
    header={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}#反反爬机制
    html=requests.get(homepage_url,header).content
    bs=BeautifulSoup(html,'lxml')
    url=bs.find_all('a',class_="list-group-item")#a标签class=‘list-group-item’
    for u in url:
        url=re.findall(r'href="(.*?)"',str(u))#a标签class=‘list-group-item’中href后面的网址
        page_url.append(url)
    return page_url

def get_pic_url(page_url):#所有连接中的Url地址
    global all_img_url
    html=requests.get(page_url).content
    url=etree.HTML(html)
    items=url.xpath('//div[@class="artile_des"]')#找到div块
    for item in items:
        img_url=item.xpath('table/tbody/tr/td/a/img/@onerror')#div块下找网址
        # Multithreading_save_img(img_url)
        for iu in img_url:
            iu='http:'+iu.split('=')[1][1:-1]#网址是this.src='//img.doutula.com/production/uploads/image/2017/05/15/20170515863654_UlAdaj.jpg'  =分隔 取后面及前后“” 加上http：
            all_img_url.append(iu)
    return img_url

def save_img(all_img_url):#保存图片
    global x
    x+=1
    save_html=requests.get(all_img_url).content
    with open('E://code/python/crawler/img/%s.jpg'%x,'wb') as f:#下载地址 命名x为全局变量 名称1.jpg  2.jpg.....
        f.write(save_html)

# def Multithreading_save_img(img_url):
#     for i in img_url:
#         th=threading.Thread(target=save_img,args=(i,))
#         th.start()

homepage_url='https://www.doutula.com/article/list/?page={}'
all_img_url=[]
x=1
for i in range(1):
    for pu in get_page_url(homepage_url.format(i)):
        get_pic_url(pu[0])#所有地址在列表中，拿出字符串
for aiu in all_img_url:
    save_img(aiu)
