print("[1m ' Web-Scraping  Using  BeautifulSoup ")

from bs4 import BeautifulSoup
import re
from urllib.request import urlopen


#url="http://py4e-data.dr-chuck.net/comments_1548643.html"
url=input("[1m Enter the Link :- ")
#read= requests.get(url)
html_content=urlopen(url)
#print("Readed data:",read)
#html_content=read.content
print(" HTML CONTENT"," \n",html_content)
soup=BeautifulSoup(html_content,"html.parser")
print(soup.prettify())
print(soup.title)

tags=soup('span')
print(tags)

num_list=[]
sum=0
count=0
for tag in tags:
    line=str(tag)
    number=re.findall('\d+',line)
    num_list.append(number)
    for num in number:
      num=int(num)
      count+=1
      sum+=num
#print(num_list)
print("Count:",count)
print(len(num_list))
print("Sum:",sum)