import pandas as pd

# data = pd.read_csv(r"Day25\weather_data.csv")
# import csv
# with open("Day25\weather_data.csv") as data:
#     data_list = csv.reader(data)
#     temprature = []
#     for row in data_list:
#         if row[1] != 'temp':  
#             temprature.append(int(row[1]))
#     print(temprature)


# temp_list = data["temp"].to_list()
# sum = 0
# for i in temp_list:
#     sum += i
# print("The Avg of Tempratures is: " + f"{round(sum/len(temp_list), 2)}")

# print(data[data.temp == data["temp"].max()])

# temp_c = data[data.day == "Monday"].temp[0]
# temp_f = ( temp_c * 9/5) + 32
# print(temp_f)

shitload_of_data = pd.read_csv(r"Day25\squirrel_data.csv")
color_list = shitload_of_data["Primary Fur Color"].to_list()
num_of_squirrel = {}
for i in color_list:
    num_of_squirrel.setdefault(i, 0)
    num_of_squirrel[i] += 1
squirrel_df = pd.DataFrame(list(num_of_squirrel.items()), columns=["Fur Color", "Count"])
squirrel_df["Fur Color"] = squirrel_df["Fur Color"].fillna("Untracked")
squirrel_df.to_csv(r"Day25\final_data.csv")
