import requests
from bs4 import BeautifulSoup

page=input('输入想导出前多少页')
url='http://www.pythontab.com/html/pythonhexinbiancheng/'
class GetText():#获得所有页面链接
    def get_pageurl(url,page):#获取所有页面主页面
        allpage=[]
        allpage.append(url+'index.html')
        for i in range (2,int(page)+1):
            allpage.append(url+str(i)+'.html')
        return allpage
    def get_url(allpage):#获得所有url并保存到字典{'title':'xxx','link':'xxx'}
         title_link=[]
         for i in allpage:
            html=requests.get(i).text
            soup=BeautifulSoup(html,'html.parser')
            titles=soup.select('#catlist > li > a')
            links=soup.select('#catlist > li > a')
            for title,link in zip(titles,links):
                data={'title':title.get_text(),'link':link.get('href')}
                title_link.append(data)
         return(title_link)
    def get_content(title_link):#获得页面内容
        for i in title_link:
            html=requests.get(i['link']).text
            soup=BeautifulSoup(html,'html.parser')
            content=soup.select('div.content > p')
            content_new=[]
            for l in content:#l的type是Tag
                content_new.append(l.get_text().encode('utf-8'))#之前写成content_new.append(l)  l的type是Tag要提取
            title_text=i['title']
            title_text=title_text.replace('*','').replace('/','').replace('"','')
            with open('e://%s.txt'%title_text,'wb') as f:
                for a in content_new:
                    f.write(a)#32行不那么写 这里会报错
                f.close()





a=GetText.get_pageurl(url,page)

b=GetText.get_url(a)
GetText.get_content(b)
