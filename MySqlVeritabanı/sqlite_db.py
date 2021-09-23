import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.cursor()

sql = "select * from customers"
cursor.execute(sql)
result = cursor.fetchall()
print(result)

for i in result:
    print(i[1]+ ' ' + i[2])

connection.close()

