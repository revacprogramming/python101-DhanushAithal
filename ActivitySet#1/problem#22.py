from urllib.request import Request,urlopen
from bs4 import BeautifulSoup

url=input('\033[1m Enter the Link \033[0m ->')
#count=int(input("Enter the count(Repeatation): "))
#pos=int(input("Enter the position :"))
#url='http://py4e-data.dr-chuck.net/known_by_Karima.htm'
html_content=urlopen(url)
#print(html_content)

soup=BeautifulSoup(html_content,"html.parser")
all_links=[]
for link  in soup.find_all('a'):
    #print(link.get('href'))
    all_links.append(link.get('href'))
for i in range(7):
    url = Request(all_links[17])
    html_content = urlopen(url)
    soup = BeautifulSoup(html_content,"html.parser")
    for title in soup.find_all("title"):
        print(title.get_text())
    all_links.clear() 
    for i in soup.find_all('a'):
        all_links.append(i.get('href'))