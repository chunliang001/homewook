###一、ALS都有哪些应用场景
__ 常用的应用场景有电影推荐、商品推荐、广告推荐
   原理就是给各个指标，判定等加权，然后将这些训练集输入ALS，包括其他的参数，内部进行矩阵相乘，给用户对未知，未点击的商品也给一个分数，就是喜好程度，然后把喜好程度的商品推荐给用户。
###二、ALS进行矩阵分解的时候，为什么可以并行化处理
__ ALS推荐系统的主要矩阵分解方法是采用交替最小二乘，矩阵分解的最终任务是找到两个矩阵P和Q，其中P和Q都是未知的，如果知道其中一个的话，就能按照线性代数标准解法求得。所以矩阵的求解，是把P当作已知，求解Q，把Q当作已知，求解P，这两个过程交替进行，直到误差达到可以接受为止。

###三、梯度下降法中的批量梯度下降（BGD），随机梯度下降（SGD），和小批量梯度下降有什么区别（MBGD）
+ 批量梯度下降法，每一次迭代时使用所有样本来进行梯度的更新；
+ 随机梯度下降，每次迭代使用一个样本来对参数进行更新，使得训练速度加快，不利于并行实现；
+ 小批量梯度下降，是对批量梯度下降以及随机梯度下降的一个这种办法。其次迭代使用batch_size个样本来对参数进行更新，优点，减小了收敛的迭代次数，可实现并行化

### 你阅读过和推荐系统/计算广告/预测相关的论文么？有哪些论文是你比较推荐的，可以分享到微信群中
+ 阅读过广告相关的推荐系统，Parallel FP-Growth for Query Recommendation、京东电商广告和推荐系统的机器学习系统实践，已分享到微信群

