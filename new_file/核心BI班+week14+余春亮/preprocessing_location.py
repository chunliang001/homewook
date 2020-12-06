import requests
import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup
import time

# def get_page_content(request_url):
#     #得到页面内容
#     header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
#     html=requests.get(request_url,headers=header,timeout=10)
#     content=html.text
#     soup=BeautifulSoup(content,'html.parser',from_encoding='utf-8')
#     return soup
#
# request_url="https://ditie.mapbar.com/beijing_line/"
# soup=get_page_content(request_url)
# subways=soup.find_all('div',class_='station')
#
# df=pd.DataFrame(columns=['name','site'])
# for subway in subways:
#     #得到线路名称
#     route_name=subway.find('strong',class_='bolder').text
#     #找到线路中，每一站的名称
#     routes=subway.find('ul')
#     routes=routes.find_all('a')
#     for route in routes:
#         temp={'name':route.text,'site':route_name}
#         df=df.append(temp,ignore_index=True)
#
# df['city']='北京'
# df.to_excel('./subway.xlsx',index=False)

# 添加经度longitude,维度 latitude

def get_location(keyword,city):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
    request_url='http://restapi.amap.com/v3/place/text?key=31bb2b7831c8588465c41ab947e213ac&keywords='+\
                keyword+'&types=&city='+city+'&children=1&offset=1&page=1&extensions=all'
    data=requests.get(request_url,headers=header)
    data.encoding='utf-8'
    data=data.text
    """
     .* 具有贪婪的性质，首先匹配到不能匹配为止
    """
    pattern='location":"(.*?),(.*?)"'
    result=re.findall(pattern,data)
    try:
        return result[0][0],result[0][1]
    except:
        return get_location(keyword.replace('站',''),city)

def work():
    df=pd.read_excel('./subway.xlsx')
    df['longitude'],df['latitude']=None,None

    for index,row in df[0:1].iterrows():
        longitude,latitude=get_location(row['name'],row['city'])
        df.iloc[index]['longitude']=longitude
        df.iloc[index]['latitude']=latitude
        sleep_time=np.random.randint(100,200)/100
        time.sleep(sleep_time)
        print(index,row['name'],longitude,latitude)
    df.to_excel('./subway.xlsx',index=False)