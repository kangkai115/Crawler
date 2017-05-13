import re
import requests
url='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&p=1'
html=requests.get(url).text

info=re.findall('<li class="newlist_deatil_two"><span>(.*?)</span><li ',html,re.S)
info_new=[]
for i in info:
    info_new.append(i.replace('</span><span>',''))
name=re.findall(' target="_blank">(.*?) ',html,re.S)
name_new=name[2:62]
name_new1=[]
for i in  name_new:
    name_new1.append(i.replace('</a></td>',''))
f=open('d:\\zhilian.txt','w')
n=1
for b in range (60):
   f.write(str(n)+name_new1[b]+info_new[b]+'\n')
   n+=1
f.close()
