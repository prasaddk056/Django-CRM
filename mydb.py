import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "newuser",
    password = "password",
    auth_plugin = "mysql_native_password"
)


cursor = db.cursor()

cursor.execute("CREATE DATABASE crmbase")

print("Database Created")