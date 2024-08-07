import pandas as pd

data = {
    '이름' : ['Alice','Bob','Carl'],
    '나이' : [25,30,29],
    '성별' : ['여','남','남']
}
df = pd.DataFrame(data, index=['A','B','C'])
print(df)
# df.to_csv('./data.csv')