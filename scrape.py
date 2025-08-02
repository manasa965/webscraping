pip install beautifulsoup4


import requests
url="https://quotes.toscrape.com"
response=requests.get(url)
print(response.status_code)
from bs4 import BeautifulSoup
soup=BeautifulSoup(response.content,"html.parser")
print(quote.text)
quotes=soup.find_all("span",class_="text")
quotes=[quote.text[1:-1] for quote in quotes]
print(quotes)
authors=soup.find_all("small",class_="author")
authors=[author.text for author in authors]
print(authors)
tags=soup.find_all("div",class_="tags") 
print(tags[0])
for i in tags[0].find_all('a',class_="tag"):
  print(i.text)
total_tags=[]
for i in range(len(tags)):
  k=[]
  for j in tags[i].find_all('a',class_="tag"):
    k.append(j.text)
  total_tags.append(','.join(k))

print(total_tags)









import pandas as pd
dataset=pd.DataFrame()
dataset['Quote']=quotes
dataset['Tags']=total_tags
dataset['Author']=authors
dataset

dataset.to_csv('quotes.csv')


