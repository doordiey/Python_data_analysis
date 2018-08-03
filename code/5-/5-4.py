#-*- coding:utf-8 -*-

import pandas as pd
from sklearn.cluster import  KMeans

inputfile = '../../data/5-/consumption_data.xls'
outputfile = '../../data/5-/data_type.xls'
k = 3 #聚类的类别
iteration = 500
data = pd.read_excel(inputfile,index_col='Id')
data_zs = 1.0*(data-data.mean())/data.std()  #数据归一化处理
model = KMeans(n_clusters= k ,n_jobs=4,max_iter=iteration)
model.fit(data_zs)

r1 = pd.Series(model.labels_).value_counts()#统计各个类别数目
r2 = pd.DataFrame(model.cluster_centers_)#找出聚类中心
r = pd.concat([r2,r1],axis=1) #横向连接
r.columns = list(data.columns) + [u'类别数目']#重命名表头
print(r)

r = pd.concat([data,pd.Series(model.labels_,index= data.index)],axis=1)
r.columns = list(data.columns) + [u'聚类类别']
r.to_excel(outputfile)