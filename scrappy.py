from urllib import request
import requests
from bs4 import BeautifulSoup
req=requests.get("https://orbzii.com/food-drink/")
soup=BeautifulSoup(req.content,"html.parser")

result=soup.find_all('li',attrs={'class':'menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-13124'})
art=soup.find_all('div',attrs={'class':'post-entry-content'})
print(result)
str1=str(result)
total=0
count=str1.split()
for i in count:
    if 'href' in i :
        #print((i[5:]))
    
        j=i[6:].split('>')
        k=len(j[0])
        print((j[0])[:k-1])
        total+=1
print(total)
print(art)


