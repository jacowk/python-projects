#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:47:14 2020

@author: jaco
"""

import matplotlib.pyplot as plt
import MySQLdb as mysql

# Total arrests per age group

table_name = "nypd_arrests_2015"

db = mysql.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="password",     # password
                     db="python_base")   # name of the database

sql = "select count(na.id) as cnt, na.age_group  \
        from {} na \
        group by na.age_group\
        order by cnt desc;".format(table_name)
        
cursor = db.cursor()

result_dict = {}

try:
   # Execute the SQL command
   cursor.execute(sql)
   results = cursor.fetchall()
   cnt = 1
   for row in results:
       result_dict[row[1]] = row[0]
except Exception as e:
   # Rollback in case there is any error
   print ("An error occured: {}".format(str(e)))

db.close()

# Prepare graph data
age_group_labels = ['<18', '18-24', '25-44', '45-64', '65+']
x_age_group = []
xt_age_group = []
y_cnt = []

cnt = 1
for age_group in age_group_labels:
    x_age_group.append(cnt)
    xt_age_group.append(age_group)
    y_cnt.append(result_dict[age_group])
    cnt += 1

print(x_age_group)
print(xt_age_group)
print(y_cnt)

# Prepare the plot
"""plt.plot(x_age_group, y_cnt)
plt.xticks(x_age_group, xt_age_group)
plt.xlabel("Age Group")
plt.ylabel("No of arrests")
plt.title("Total Arrests Per Age Group")
plt.show()"""

# Prepare bar chart
plt.bar(x_age_group, y_cnt, align='center')
plt.xticks(x_age_group, xt_age_group)
plt.show()
