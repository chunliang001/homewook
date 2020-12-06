import route_api
import preprocessing_location
import pandas as pd

# site1='五道口站'
# site2='北京南站'
# shortest_path=route_api.compute(site1,site2)
# print(shortest_path)

# 找到最近的地铁站
def get_nearest_subway(data,longitude1,latitude1):
    #保存当前最小距离
    distance=float('inf')
    longitude1,latitude1=longitude1,latitude1
    nearst=None
    for i in range(data.shape[0]):
        site1=data.iloc[i]['name']
        longitude=float(data.iloc[i]['longitude'])
        latitude=float(data.iloc[i]['latitude'])
        temp=(float(longitude1)-longitude)**2+(float(latitude1)-latitude)**2
        if temp<distance:
            distance=temp
            nearest=site1
    return nearest


def compute(site1,site2):
    longitude1,latitude1=preprocessing_location.get_location(site1,city)
    longitude2,latitude2=preprocessing_location.get_location(site2,city)
    # 加载所有的地铁线路
    data=pd.read_excel('./subway.xlsx')
    #求site1,site2最近的地铁站
    start=get_nearest_subway(data,longitude1,latitude1)
    end=get_nearest_subway(data,longitude2,latitude2)
    print('{}最近的地铁站为{}'.format(site1,start))
    print('{}最近的地铁站为{}'.format(site2,end))
    shortest_path=route_api.compute(start, end)
    if site1!=start:
        shortest_path.insert(0,site1)
    if site2!=end:
        shortest_path.append(site2)
    print('从{}=》{}的最优路径为:\n {}'.format(site1,site2,shortest_path))

if __name__ == '__main__':
    city='北京'
    site1='清华大学'
    site2='798'
    compute(site1,site2)