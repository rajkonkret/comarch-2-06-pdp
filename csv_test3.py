import pandas as pd
# pip install pandas

data = pd.read_csv('records.csv')

print(data)
#     name branch  year  cgpa
# 0  Radek    COE     2   9.1

print(data.columns)
print(data.values)  # [['Radek' 'COE' 2 9.1]]
print(data.values[0])  # ['Radek' 'COE' 2 9.1]
print(data.items)