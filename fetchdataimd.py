from bs4 import BeautifulSoup
import requests
import pandas as pd


url ='https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'# 'https://enam.gov.in/web/dashboard/trade-data'

r=requests.get(url)
#print(r)

soup=BeautifulSoup(r.text,"lxml")#("html.parser")

# print(soup)
# data=soup.find_all("div",class_="col-sm-4 col-lg-4 col-md-4")
# print(len(data))

names=soup.find_all("a",class_="title")
print(len(names))

# dic={'Tablets Name':"",'Price':""}

fianl_list=[]

for i in range(len(names)):
    dic={'Tablets Name':"",'Price':""}
    dic["Tablets Name"].append(name.text)
    dic["Price"].append(price.text)
    
    
    
    
    
# print(names)
for name in names:
    
    dic["Tablets Name"].append(name.text)
    
prices=soup.find_all("h4",class_="pull-right price")
for price in prices:
   dic["Price"].append(price.text)
   

# print(dic)




# df=pd.DataFrame.from_dict(dic)
# df.to_csv("Tablet_name_and_price.csv",index=True)
    

