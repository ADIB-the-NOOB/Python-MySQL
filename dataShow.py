import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="hacker",
  database = "mydb001"
)
mycursor = mydb.cursor()

sql = "DELETE * FROM username"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
