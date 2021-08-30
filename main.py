import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="hacker",
  database = "mydb001"
)
mycursor = mydb.cursor()

while True:
  sql = "INSERT INTO username (name, address) VALUES(%s, %s)"
  a = input("Name:")
  b = input("Address:")
  val = (a , b)

  mycursor.execute(sql , val)

  mydb.commit()

  print(mycursor.rowcount , "Inserted")

  mycursor.execute("SELECT * FROM username")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)