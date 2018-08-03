#-*- coding: utf-8 -*-
import pandas as pd
from sklearn.tree import  DecisionTreeClassifieras as  DTC
from sklearn.tree import  export_graphviz

filename = '../../data/5-/sales_data.xls'
data = pd.read_excel(filename,index_col=u'序号')

#结合实际问题，用1表示“好”“是”“高”三个属性，剩余属性用-1表示。
data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = -1
x = data.iloc[:,:3].as_matrix().astype(int)
y = data.iloc[:,3].as_matrix().astype(int)

dtc = DTC(criterion = 'entropy')
dtc.fit(x,y)
print(type(x))
#可视化决策树
#导出结果为dot文件，需要安装Graphviz转换为其他格式。直接word文档默认也能打开查看，但不是具体的表的形式，而是文字形式。
with open("tree.dot",'w') as f:
	f = export_graphviz(dtc,feature_names= data.columns[:3] ,out_file= f)
