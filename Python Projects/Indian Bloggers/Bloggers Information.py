import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

url="https://indianbloggers.org/"
r=requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,"html.parser")
print(soup.prettify)

dic={"Names":[],"Links":[]}
category={"blogspot":0,"wordpress":0,"others":0,"facebook":0,"twitter":0,"youtubers":0}
anch=soup.findAll("a")
print(anch)

for items in anch:
    print(items)

    if len(items.text)>0 and bool(re.match("^http",items['href'])):
        dic["Names"].append(items.text)
        dic["Links"].append(items['href'])
        if re.search("blogspot",items["href"]):
            category["blogspot"]+=1
        elif re.search("wordpress",items["href"]):
            category["wordpress"]+=1
        elif re.search("facebook",items["href"]):
            category["facebook"]+=1
        elif re.search("twitter",items["href"]):
            category["twitter"]+=1
        elif re.search("youtube",items["href"]):
            category["youtubers"]+=1
        else:
            category["others"]+=1
print(category)
data=pd.DataFrame(dic).set_index("Names")

plt.bar(category.keys(),category.values())
plt.show()

platform=["blogspot","wordpress", "twitter","youtubers","others"]
values=[107,49,2,11,221]
plt.pie(values,labels=platform,shadow=True,autopct="%.2f")
plt.show()







