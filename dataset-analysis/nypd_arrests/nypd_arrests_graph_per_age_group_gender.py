#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:47:14 2020

@author: jaco
"""

import numpy as np
import matplotlib.pyplot as plt
import MySQLdb as mysql

# Total arrests per age group

table_name = "nypd_arrests_2015"
gender_list = ['M', 'F']
data = []

db = mysql.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="password",     # password
                     db="python_base")   # name of the database
        
cursor = db.cursor()

for gender in gender_list:
    sql = "select count(na.id) as cnt, na.age_group \
        from {} na \
        where na.perp_sex = '{}' \
        group by na.age_group \
        order by cnt desc;".format(table_name, gender)
    result_dict = {}

    try:
       # Execute the SQL command
       cursor.execute(sql)
       results = cursor.fetchall()
       cnt = 1
       for row in results:
           result_dict[row[1]] = row[0]
       data.append(result_dict)
    except Exception as e:
       # Rollback in case there is any error
       print ("An error occured: {}".format(str(e)))

db.close()

# Prepare graph data
age_group_labels = ['<18', '18-24', '25-44', '45-64', '65+']
x_age_group = list(range(0, len(age_group_labels)))
final_data = []
for x in range(0, len(data)):
    final_sub_data = []
    for age_group in age_group_labels:
        value = data[x][age_group]
        final_sub_data.append(value)
    final_data.append(final_sub_data)

print(age_group_labels)
print(x_age_group)
print(final_data)

# Prepare bar chart
X = np.arange(0, len(age_group_labels))
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X + 0.00, final_data[0], color = 'b', width = 0.25)
ax.bar(X + 0.25, final_data[1], color = 'g', width = 0.25)
ax.legend(labels = gender_list)
ax.set_xticks(X, age_group_labels) Not working yet
ax.set_ylabel('Total Arrests')
ax.set_title('Total NYPD Arrests by Gender')
plt.show()