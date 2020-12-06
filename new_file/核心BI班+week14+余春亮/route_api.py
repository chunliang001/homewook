import pandas as pd
import requests
import re

# # 数据加载
# data=pd.read_excel('./subway.xlsx')
#
# #计算两点之间距离
# def compute_distance(longtitue1,latitude1,longitude2,latitude2):
#     header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
#     request_url='http://restapi.amap.com/v3/distance?key=31bb2b7831c8588465c41ab947e213ac&origins='+\
#                 str(longtitue1)+","+str(latitude1)+'&destination='+str(longitude2)+','+str(latitude2)+"&type=1"
#     data=requests.get(request_url,headers=header)
#     data.encoding='utf-8'
#     data=data.text
#     pattern='distance":"(.*?)","duration":"(.*)"'
#     result=re.findall(pattern,data)
#     return result[0][0]
#
#
# #compute_distance(116.337581,39.993138,116.339941,39.976228)
#
#
# from collections import defaultdict
# # 保存图中两点间距离
# graph=defaultdict(dict)
#
# for i in range(data.shape[0]):
#     site1=data.iloc[i]['site']
#     if i<data.shape[0]-1:
#         site2=data.iloc[i+1]['site']
#         #如果是同一条线路
#         if site1==site2:
#             longitude1,latitude1=data.iloc[i]['longitude'],data.iloc[i]['latitude']
#             longitude2,latitude2=data.iloc[i+1]['longitude'],data.iloc[i+1]['latitude']
#             name1=data.iloc[i]['name']
#             name2=data.iloc[i+1]['name']
#             # 按照距离，计算两点之间的距离
#             distance=compute_distance(longitude1,latitude1,longitude2,latitude2)
#             graph[name1][name2]=distance
#             graph[name2][name1]=distance
#             print(name1,name2,distance)
# #
# import pickle
# output=open('graph.pkl','wb')
# graph=pickle.dump(graph,output)

import pickle
file=open('graph.pkl','rb')
graph=pickle.load(file)


# 找到开销最小的节点
def find_lowest_cost_node(costs):
    # 初始化数据
    lowest_cost = float('inf')  # 打擂法，初始化最小值 inf
    lowest_cost_node = None
    # 遍历所有节点
    for node in costs:
        if not node in processed:
            # 如果当前节点的开销比已经存在的开销小，那么就更新节点为开销最小的节点
            if costs[node] < lowest_cost:
                lowest_cost = costs[node]
                lowest_cost_node = node
    return lowest_cost_node

#找到最短路径
def find_shortest_path():
    node=end
    shortest_path=[end]
    while parents[node]!=start:
        # 往前移动一步
        node=parents[node]
        #往前移动一步，添加到路径中
        shortest_path.append(node)
    shortest_path.append(start)
    return shortest_path

# 计算图中从start到end的最短距离
def dijkstra():
    #查询到目前开销最小的节点(从U种)
    node=find_lowest_cost_node(costs)
    #print('当前cost最小节点:',node)
    #使用找到的开销最小节点，计算它的邻居，是否可以通过它进行更新
    #如果所有节点，都在processed，就结束
    while node is not None:
        #获取节点的cost
        cost=costs[node] # cost 是node到start
        #获取节点的邻居
        neighbors=graph[node]
        #遍历所有邻居，看是否可以通过它进行更新
        for neighbor in neighbors.keys():
            #计算邻居到当前节点+当前节点开销
            new_cost=cost+float(neighbors[neighbor])
            if neighbor not in costs or new_cost<costs[neighbor]:
                costs[neighbor]=new_cost
                #经过node达到neighbor节点，cost更少
                parents[neighbor]=node
        #将当前节点，标记为已处理
        processed.append(node)
        #下一步，继续找U中最短距离的节点 costs=U,processed=S
        node=find_lowest_cost_node(costs)
        #print('当前状态最小节点:',node)
    #循环完，说明所有节点处理完毕
    startest_path=find_shortest_path()
    startest_path.reverse()
    return startest_path
    #print('从{}到{}的最短路径:{}'.format(start,end,startest_path))


# start='五道口站'
# end='首经贸站'
# #创建节点的开销表,cost是指从start到该节点的距离
# costs={}
# #存储父节点的Hash表，用于记录路径
# parents={}
# parents[end]=None
#
# #获取节点相邻的节点
# for node in graph[start].keys():
#     costs[node]=float(graph[start][node])
#     parents[node]=start
# # 终点到起点，设置无穷大
# costs[end]=float('inf')
# print(graph[start].keys())
#
# processed=[]
#
# dijkstra()

def compute(site1,site2):
    global start,end,costs,parents,processed
    start = site1
    end = site2
    # 创建节点的开销表,cost是指从start到该节点的距离
    costs = {}
    # 存储父节点的Hash表，用于记录路径
    parents = {}
    parents[end] = None

    # 获取节点相邻的节点
    for node in graph[start].keys():
        costs[node] = float(graph[start][node])
        parents[node] = start
    # 终点到起点，设置无穷大
    costs[end] = float('inf')
    processed = []
    shortest_path=dijkstra()
    return shortest_path

if __name__ == '__main__':
    site1='五道口站'
    site2='北京南站'
    shortest_path=compute(site1,site2)
    print(shortest_path)
