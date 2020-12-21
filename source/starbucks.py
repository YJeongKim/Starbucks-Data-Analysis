import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import datetime
import time
from itertools import count
import ssl

def get_request_url(url, enc='utf-8'):
    
    req = urllib.request.Request(url)

    try:
        ssl._create_default_https_context = ssl._create_unverified_context  

        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            try:
                rcv = response.read()
                ret = rcv.decode(enc)
            except UnicodeDecodeError:
                ret = rcv.decode(enc, 'replace')    
            
            return ret
            
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None



def Starbucks_Menu(result):
    Starbucks_URL = 'https://www.starbucks.co.kr/menu/drink_list.do'    

    
    wd = webdriver.Chrome('/Users/imkyunghwan/Documents/CRWL/201109/chromedriver')

    wd.get(Starbucks_URL)
    time.sleep(10)

           
    rcv_data = wd.page_source        
    soupData = BeautifulSoup(rcv_data, 'html.parser')
    coffeeMenu = soupData.select('.product_list dd ul li dl dd')
    for dd in coffeeMenu:
        result.append(dd.string)
        print(dd.string)

    
    
        
    return

def cswin_Starbucks():
    
    result =[]
    print('Starbucks ADDRESS CRAWLING START')
    Starbucks_Menu(result)
    starbucks_table = pd.DataFrame(result)
    starbucks_table.to_csv("./starbucks.csv", encoding="cp949", mode='w', index=True)

    print('FINISHED')

    
    
if __name__ == '__main__':
     cswin_Starbucks()

