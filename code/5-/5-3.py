#-*- coding:utf-8 -*-
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense,Activation

inputfile = '../../data/5-/sales_data.xls'
data = pd.read_excel(inputfile,index_col=u'序号')


def cm_plot(y, yp):
  from sklearn.metrics import confusion_matrix #导入混淆矩阵函数
  cm = confusion_matrix(y, yp) #混淆矩阵
  import matplotlib.pyplot as plt #导入作图库
  plt.matshow(cm, cmap=plt.cm.Greens) #画混淆矩阵图，配色风格使用cm.Greens，更多风格请参考官网。
  plt.colorbar() #颜色标签
  for x in range(len(cm)): #数据标签
    for y in range(len(cm)):
      plt.annotate(cm[x,y], xy=(x, y), horizontalalignment='center', verticalalignment='center')
  plt.ylabel('True label') #坐标轴标签
  plt.xlabel('Predicted label') #坐标轴标签





#数据预处理
data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = 0
x = data.iloc[:,:3].as_matrix().astype(int)
y = data.iloc[:,3].as_matrix().astype(int)

model = Sequential()
model.add(Dense(3,10)) #输入节点到隐藏节点
model.add(Activation('relu')) #在隐藏层运用relu激活函数
model.add(Dense(10,1))  #隐藏节点到输出层
model.add(Activation('sigmoid'))#输出值为0-1,故用sigmoid函数作为激活函数
#以上一层层堆叠而成。
model.compile(loss = 'binary_crossentropy',optimizer= 'adam',class_code = 'binary')#编译模型

model.fit(x,y,nb_spoch = 1000,betch_size = 10)#学习一千次
yp = model.predict_classes(x).reshape(len(y))

cm_plot(y,yp).show() #可视化结果
