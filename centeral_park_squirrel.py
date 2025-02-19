import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250219.csv')
# print(data.columns)
# print(data['Primary Fur Color'])

x= data['Primary Fur Color'].value_counts()
x.to_csv('fur_color_count.csv')
