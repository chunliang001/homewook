# 1、常用的路径规划算法有哪些?
Dijkstra算法、Floyd、贪心算法、模拟退火等

# 2、推荐系统的架构是怎样的？
推荐系统包含的层级比较多，整个线上推荐系统包含：最上层线上推荐服务、中层各个推荐数据召回集（数据主题、分类池子）、底层各种推荐模型。

# 3、你都了解推荐系统中的哪些常用算法？原理是怎样的？
常见的算法有协同过滤、关联规则、图算法等
+ 协同过滤，常见的模型有Baseline、SlopeOne、surprise
基于物品的协同过滤，当目标用户需要推荐时，可以先通过兴趣、爱好或行为习惯找到与他相似的其他用户，然后把那些与目标用户相似的用户喜欢的并且目标用户没有浏览过的物品推荐给目标用户。
基于物品的协同过滤推荐算法，1）分析各个用户对物品的浏览记录；2）依据浏览记录分析得出所有物品之间的相似度；3）对于目标用户评价高的物品，找出与之相似度最高的K个物品；4）将这K个物品中目标用户没有浏览过的物品推荐给目标用户
+ 关联规则 常见算法包有Apriori、mlxtend.frequent_patterns 
关注产品和产品之间的关联性，基于频繁项集的的一类推荐算法
+ 图算法 常见的有PageRank、DeepWalk、Node2Vec、GCN
PageRank 用于网页重要性的分析，一个网页的影响力等于所有入链集合的页面的加权影响力之和
Graph Embedding 常见的有DeepWalk、Node2Vec模型
将所有user在一段时间内的消费历史构建为一个图，提取提取靠RandomWalk生成模型
GCNs 基于非欧空间的数据建立拓扑关联	
