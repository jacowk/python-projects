import mysql.connector as mysql
import matplotlib.pyplot as plt

# Create database connection
db = mysql.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="password",     # password
                     db="python_base")   # name of the database

# Prepare SQL statement
sql = "select count(ad.id) as cnt, ad.age\
        from accidental_drug ad\
        where ad.race like 'White'\
        group by ad.age\
        order by cnt desc\
        limit 10;"

cursor = db.cursor()

result_dict = {}

try:
   # Execute the SQL command
   cursor.execute(sql)
   results = cursor.fetchall()
   cnt = 1
   for row in results:
       print(row)
       result_dict[row[1]] = row[0]
except Exception as e:
   # Rollback in case there is any error
   print ("An error occured: {}".format(str(e)))

db.close()

# Prepare graph data
race_labels = ['White', 'Hispanic White', 'Black', 'Hispanic Black', 'Unknown', 'Asian Other', 'Asian Indian', 'Other',
               'Chinese', 'Hawaiian', 'Native American Other']
x_race = []
xt_race = []
y_cnt = []

cnt = 1
for race_label in result_dict.keys():
    x_race.append(cnt)
    xt_race.append(race_label)
    y_cnt.append(result_dict[race_label])
    cnt += 1

# Prepare bar chart
plt.barh(x_race, y_cnt, align='center')
plt.yticks(x_race, xt_race)
plt.show()
