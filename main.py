# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# temperatures = []
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         temperatures.append(row[1])
#     temperatures.pop(0)
#     temperatures = list(map(int, temperatures))
#     print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(data["temp"])

data_dict = data.to_dict()
# print(data_dict)

temp_list = data['temp'].to_list()
# print(temp_list)

mean = data['temp'].mean()
# print(mean)

max_value = data['temp'].max()
# print(max_value)

