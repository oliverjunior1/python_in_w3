# import mysql.connector

# mydb = mysql.connector.connect(
#     host='localhost',
#     user = 'yourusername',
#     password = 'yourpassword'
# )

# mycursor = mydb.cursor()

# mycursor.execute('CREATE DATABASE mydatabase')

#################################################

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
