import mysql.connector as mysql
import matplotlib.pyplot as plt

# Create database connection
db = mysql.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="password",     # password
                     db="python_base")   # name of the database

drug_types = [ 'heroin','cocaine','fentanyl','fentanylanalogue','oxycodone','oxymorphone','ethanol','hydrocodone','benzodiazepine','methadone','amphet','tramad','morphine_notheroin','hydromorphone','other','opiatenos','anyopioid' ]

result_dict = dict()

for drug_type in drug_types:
    # Prepare SQL statement
    sql = "select count(ad.id) as cnt, ad.{} \
            from accidental_drug ad \
            where ad.{} = true \
            and ad.race like 'Black' \
            group by ad.heroin \
            order by cnt desc;".format(drug_type, drug_type)

    cursor = db.cursor()

    try:
       # Execute the SQL command
       cursor.execute(sql)
       results = cursor.fetchall()
       cnt = 1
       for row in results:
           result_dict[drug_type] = row[0]
    except Exception as e:
       # Rollback in case there is any error
       print ("An error occured: {}".format(str(e)))

db.close()

#print(result_dict)
for drug_type in sorted(result_dict):
    print(drug_type, result_dict[drug_type])


# Prepare graph data
x_drug_type = []
xt_drug_type = []
y_cnt = []

cnt = 1

for drug_type in result_dict.keys():
    x_drug_type.append(cnt)
    xt_drug_type.append(drug_type)
    y_cnt.append(result_dict[drug_type])
    cnt += 1

# Prepare bar chart
plt.barh(x_drug_type, y_cnt, align='center')
plt.yticks(x_drug_type, xt_drug_type)
plt.show()
