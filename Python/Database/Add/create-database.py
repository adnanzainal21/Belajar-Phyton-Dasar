import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",    
)
   
cursor = db.cursor()
cursor.execute("create database usershop")
# create ( add )
# drop ( hapus )

print("Database on update")