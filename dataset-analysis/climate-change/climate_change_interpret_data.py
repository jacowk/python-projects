#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:06:48 2020

@author: jaco

https://catalog.data.gov/dataset?tags=crime
https://data.world/jaco-koekemoer/personaldataanalysis

To install mysql-connector go to Terminal in pycharm at the bottom, then type:
sudo python -m pip install mysql-connector

8599213 GlobalLandTemperaturesByCity.csv
"""
import csv #https://docs.python.org/3/library/csv.html
import utils as u
import matplotlib.pyplot as plt

print("Started")

#filename = "/home/jaco/python-data/datasets/climate_data/GlobalLandTemperaturesByCity/Aachen.csv"
filename = "/home/jaco/python-data/datasets/climate_data/GlobalLandTemperaturesByCity/Pretoria.csv"
errors = []
cnt = 1
result_dict = dict()
month = "12"
no_years = 50
page_no = 1

end = no_years * page_no
start = end - no_years

# Import csv
with open(filename, newline = '') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')

    for row in datareader:
        if cnt == 1:
            cnt += 1
            continue #Skip first line with only column names

        #print(row)

        if len(row[1]) > 0:
            Date = u.format_date(row[0])
            AverageTemperature = u.scrub_decimal(row[1])

            #Build dictionary for the selected month
            if u.is_month(Date, month):
                result_dict[Date] = AverageTemperature
                cnt += 1



# Prepare graph data
x = [] #
xt = [] #Years
y_cnt = [] #Temperatures

cnt = 1
for race_label in sorted(result_dict.keys(), reverse=False):
    if (cnt >= start and cnt <= end):
        x.append(cnt)
        xt.append(race_label)
        y_cnt.append(result_dict[race_label])
    cnt += 1

print("Done: Total: {}".format(cnt))
print("Total pages: {:f}".format(cnt / no_years))

# Prepare bar chart
plt.barh(x, y_cnt, align='center')
plt.yticks(x, xt)
plt.show()

# Prepare line chart
#plt.plot(xt,y_cnt)
#plt.title('Temparatures')
#plt.xlabel('Years')
#plt.xticks(rotation='vertical')
#plt.ylabel('Temperatures')
#plt.show()