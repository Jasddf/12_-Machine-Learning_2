import numpy as np
import pandas as pd

my_index = ['A','B','C']
my_columns = ['이름','나이','성별']
my_data = np.array([['Alice','Bob','Carl'],
                       [25,30,29],
                       ['여','남','남']]).transpose()
df = pd.DataFrame(my_data, index=my_index, columns=my_columns)
# print(df[['성별','이름']])

print(df,'\n',df.loc['A'])