import requests
from bs4 import BeautifulSoup

try:
    source=requests.get('https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=610644601173&hvpos=&hvnetw=g&hvrand=17205332483520649671&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061674&hvtargid=kwd-10573980&hydadcr=14453_2316415') 
    source.raise_for_status()
    
    soup=BeautifulSoup(source.text,'html.parser')
    print(soup)
    
    
except Exception as e:
    print(e)

