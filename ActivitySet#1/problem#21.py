import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url="http://py4e-data.dr-chuck.net/known_by_Aidan.html"
count=0
for n in range(7):
    html= urllib.request.urlopen(url).read()

soup=BeautifulSoup(html,"html.parser")
for a_tag in soup.find_all("a"):
count=count+1
if count > 18:
count=0
break
url=a_tag["href"]
print(url)