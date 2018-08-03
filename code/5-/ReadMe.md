## 代码中的一些学习。

### 5-1.py ：sklearn库就实际问题建立逻辑回归模型

##### ①对书中代码报错的一些修改。若按书中原代码会报错无法运行。

错误如下：

对data.columns[rlr.get_support()]写法报错：

*IndexError* : boolean index did not match indexed array along dimension 0; dimension is 9 but corresponding boolean dimension is 8

解决方法:

rlr.get_support()函数得到的会使一个布尔值（是否为好的特征）组成的列表。[False False  True  True False  True  True False]

将布尔值为True的列名单独组成一个列表后提取对应数据作为参数。（见代码处）

##### ②sklearn库对模型构造部分进行了封装，只需要当函数调用，了解参数都是什么意思及应用场景。

 LogisticRegression类的常用方法及参数介绍：

- fit(X, y, sample_weight=None)  x为训练样本，y为对应的标记向量即训练样本对应类别构成的向量。返回对象,self。
- score() ：返回给定测试集合的平均准确率。（浮点型数值。）

该类的详细文档：[这个。](http://sklearn.apachecn.org/cn/0.19.0/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression)

### 5-2.py：sklearn库结合实际问题运用决策树算法

##### ①书中代码报错的一些修改。若按书中原代码会报错无法运行。

书中用: x.columns.此时x为numpy.ndarray类型不存在columns.

结合参数理解：做改良改为：data.columns[:3]即为三个特征的名称列表。

常用方法及参数说明：与5-1.py中的差不多。由更多需要见详细文档。

该类的详细文档：[这里。](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)

输出效果转换为png图片后：

![没了。](https://github.com/doordiey/Python_data_analysis/tree/master/image/5-2.png) 

### 5-3.py：神经网络预测销量高低(此例未考虑过拟合问题)

涉及神经网络的搭建。每步操作在代码中由注解。

相关库：Keras     [这个](https://keras-cn.readthedocs.io/en/latest/)

输出结果为：![也没了。](https://github.com/doordiey/Python_data_analysis/tree/master/image/5-3.png)

### 5-4.py：







