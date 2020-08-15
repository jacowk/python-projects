import mysql.connector as mysql

db = mysql.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="password",     # password
                     db="python_base")   # name of the database

mycursor = db.cursor()

mycursor.execute("select * from nypd_arrests_2015")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)




