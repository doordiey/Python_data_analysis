#-*- coding:utf-8 -*-

import pandas as pd
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR

filename = '../../data/5-/bankloan.xls'
data = pd.read_excel(filename)
x = data.iloc[:,:8].as_matrix()
y = data.iloc[:,8].as_matrix()

#开始进行属性规约。
rlr = RLR() #建立随机逻辑货柜模型，筛选变量
rlr.fit(x,y)
m = list(rlr.get_support()) #获取特征筛选结果
print(u'适合的特征选出来了。如下：')
n = []
for i in range(len(m)):
	if m[i] == True:
		n.append(data.columns[i])
		print(data.columns[i])
		#columns内参数应为int型.
x = data[n].as_matrix() #将筛选好特征的数据列出
#以上进行了数据预处理中的属性规约。

#建立逻辑回归模型进行测试。
lr = LR()
lr.fit(x,y)
print(u'模型训练结束')
print(u'模型的平均正确率为：%s'% lr.score(x,y))


