
import requests
from bs4 import BeautifulSoup
import re

url='http://wanmeishijiexiaoshuo.org/book/'
#res=requests.get(url)
#res.raise_for_status()

for i in range(4477,4477):
    try:
       currenturl=url+str(i)+'.html'
       res=requests.get(currenturl)
       res.raise_for_status()
       print(currenturl)
       html=res.text
       soup = BeautifulSoup(html,'html.parser')
       b=soup.select('h1')#查找期次所在的标签
       a=soup.select('.content p')#查找期次所在的标签
       [a.extract() for a in soup('script')] 
       [a.extract() for a in soup('div')] 
       [a.extract() for a in soup('center')] 
       [a.extract() for a in soup('.center')] 
       dr = re.compile(r'<[^>]+>',re.S)
       bb= dr.sub('',str(a))
       f=open("one12.txt","a",encoding='utf-8')#将每句话写入这个txt文件中，先打开
       f.writelines('\n')
       f.writelines(str(b).replace('<h1>','').replace('</h1>',''))
       f.writelines('\n')
       f.writelines(str(bb).replace('<p>','').replace('</p>',''))
       f.close()#关闭文件
    except requests.RequestException as e:#处理异常
         print(e)
    
