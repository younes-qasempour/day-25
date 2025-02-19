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
print(data["temp"])
