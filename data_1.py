# 데이터 파일의 폴더와 작업하고 있는 폴더의 구분 중요
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

col_names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv',names=col_names)

corr = data.corr(method='pearson')
# data.describe().to_csv('./results/pima_describe.csv')
# data.corr(method ='pearson').to_csv('./results/corr.csv')

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr, cmap='coolwarm',vmin=-1,vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(col_names)
ax.set_yticklabels(col_names)
plt.show()