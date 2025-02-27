## 一、KNN与KMeans中的K分别代表什么？
+ K近邻算法(KNN)中的K表示寻找附近最近的K个点进行投票;
+ 聚类算法,KMeans中的K表示将数据集分成K类，K个簇心聚类点

## 二、都有哪些常用的启发式算法？
+ 目前通用的启发式算法有模拟退火算法、遗传算法、蚁群算法、人工神经网络等
+ 1）模拟退火算法  
   + 模拟退火算法的思想借鉴于固体的退火原理，当固体的温度很高的时候，内能比较大，固体的内部粒子处于快速无序运动，当温度慢慢降低的过程中，固体的内能减小，粒子的慢慢趋于有序，最终，当固体处于常温时，内能达到最小，此时，粒子最为稳定。
+ 2）遗传算法  
   + 遗传算法起源于对生物系统所进行的计算机模拟研究。它是模仿自然界生物进化机制发展起来的随机全局搜索和优化方法，借鉴了达尔文的进化和孟德尔的遗传学说。其本质是一种高效、并行、全局搜索的方法，能在搜索过程中自动获取和积累有关搜索空间的知识，并自适应地控制搜索过程以求得最佳解
 
## 三、遗传算法的原理是怎样的？
 + 通过模拟自然进化过程（达尔文生物进化论）搜索最优解的方法，遗传操作包括：选择、交叉和变异  
 + 算法核心：参数编码、初始群体的设定、适应度函数、遗传操作设计、控制参数设定
 + 以一种群体中的所有个体为对象，利用随机化技术指导对一个被编码的参数空间进行高效搜索
#### 遗传算法步骤：
  + 1、对潜在问题进行编码，初始化基因组，并根据基因组随机初始化种群，并指定繁衍代数。
  + 2、计算种群中每个个体的适应度，选择一定数目的留下，其余淘汰。
  + 3、在留下的个体中，随机繁衍，对分母基因进行交叉（极小概率变异），产生下一代
  + 4、回到第2步进行循环。直到达到指定的繁衍代数
 
