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
prices=soup.find_all("h4",class_="pull-right price")

name_l,price_l=[],[]
for name in names:
    name_l.append(name.text)
    
for price in prices:
    price_l.append(price.text)
# print(name_l,price_l)

# fianl_list=[]

import json

jsonList = []

for i in range(0,len(name_l)):
    jsonList.append({"Tablet_Name" : name_l[i], "Price" : price_l[i]})


print(json.dumps(jsonList, indent = 1))


# for i in range(len(name_l)):
    
#     dic={'Tablet Name':"",'Price':""}
#     dic["Tablet Name"].append(name_l[i])
#     dic["Price"].append(price_l[i])
#     fianl_list.append(dic)
    
# print(fianl_list)
    
    
    
    
    
    
# # print(names)
# for name in names:
    
#     dic["Tablets Name"].append(name.text)
    
# prices=soup.find_all("h4",class_="pull-right price")
# for price in prices:
#    dic["Price"].append(price.text)
   

# # print(dic)




# df=pd.DataFrame.from_dict(dic)
# df.to_csv("Tablet_name_and_price.csv",index=True)
    

