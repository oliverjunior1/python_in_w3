import mysql

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'yourusername',
    password='yourpassword'
)

print(mydb)