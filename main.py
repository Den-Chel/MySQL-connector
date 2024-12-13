import mysql.connector

# Connect to MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678"
)

if connection.is_connected():
    print("Connected")
else:
    print("Failed")
