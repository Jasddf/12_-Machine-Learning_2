# 데이터 파일의 폴더와 작업하고 있는 폴더의 구분 중요
import pandas as pd
import matplotlib.pyplot as plt

col_names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv',names=col_names)

data.describe().to_csv(',/results/describe.csv')