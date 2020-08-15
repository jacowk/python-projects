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

filename = "/home/jaco/python-data/datasets/climate_data/GlobalLandTemperaturesByCity/Accra.csv"
errors = []
cnt = 1
result_dict = dict()
month = "12"
no_years = 20
page_no = 1
no_pages = 0

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

# Break dict into pages
page_list = list()
temp_cnt = 1
temp_dict = dict()
for key in sorted(result_dict.keys(), reverse=False):
    if temp_cnt > no_years:
        page_list.append(temp_dict)
        temp_dict = dict()
        temp_cnt = 1
    temp_dict[key] = result_dict[key]
    temp_cnt += 1
page_list.append(temp_dict)

# Calculate average
average_dict = dict()
for temp_dict in page_list:
    total = 0
    cnt = 0
    temp_key = ''
    for key in sorted(temp_dict.keys(), reverse=False):
        total += temp_dict[key]
        cnt += 1
        temp_key = key
    average_dict[temp_key] = total / cnt

print(average_dict)
keys = sorted(average_dict.keys(), reverse=True)
last_average_key = keys[0]
second_last_average_key = keys[1]

print(last_average_key)
print(second_last_average_key)


"""
# Prepare graph data
x = [] #
xt = [] #Years
y_cnt = [] #Temperatures

cnt = 1
for average_label in sorted(average_dict.keys(), reverse=False):
    if (cnt >= start and cnt <= end):
        x.append(cnt)
        xt.append(average_label)
        y_cnt.append(result_dict[average_label])
    cnt += 1

# Prepare bar chart
plt.barh(x, y_cnt, align='center')
plt.yticks(x, xt)
plt.show()
"""
