# Using Web Services
# https://www.py4e.com/lessons/servces
import xml.etree.ElementTree as ET
from urllib.request import urlopen
#url=input("Enter the Location :")
data=" http://py4e-data.dr-chuck.net/comments_1545938.xml"
print("Retrieving "+ 'http://py4e-data.dr-chuck.net/comments_1545938.xml')
xml=urlopen(data)
xml=xml.read()
print("Retrived: "+str(len(xml))+'Character')

tree=ET.fromstring(xml)
counts=tree.findall('.//count')
print("Count: "+str(len(counts)))

n=0
for count in counts:
    n+=int(count.text)

print("Sum :"+str(n))