### 一、什么是反向传播中的链式法则
+ 误差从输出一层一层往前传播，不可以跳过某些中间步骤，在计算每一步的误差时，需要乘上上一步得到的误差（链式法则,层层相乘);在传播过程中，如果某一部分可以直接用一整个函数代替，则可以对整块求导，然后将导数数值传到上一步，这仍然符合链式求导法则。

### 二、请列举几种常见的激活函数，激活函数有什么作用
+ 常见的激活函数有:sigmod 函数,tanh 函数,Relu函数,softmax
+ 激活函数的作用：
  + 1、激活函数的特点是非线性，而数据的分布绝大多数是非线性的，这样可以强化网络的学习能力
  + 2、每一层节点的输入都是上层输出的线性函数，如果没有激活函数，输出的则都是线性组合

### 三、利用梯度下降法训练神经网络，发现模型loss不变，可能有哪些问题？怎么解决？+ 可能有哪些问题：数据集是否正常、过拟合、学习遇到瓶颈、神经网络结构设计不当
  + train loss 趋于不变，test loss 趋于不变，说明数据集100%有问题
  + train loss 不断下降，test loss 趋于不变，可能网络过拟合，过拟合可以给模型增加正则项；
  + train loss 趋势不变，test loss 趋于不变，可能学习遇到瓶颈，需要减小学习率或批量数目
