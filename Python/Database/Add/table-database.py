import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "usershop",  
)
   
cursor = db.cursor()
cursor.execute(
    """
    CREATE TABLE barang(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(50) NOT NULL,
    harga VARCHAR(50) NOT NULL,
    stok VARCHAR(50) NOT NULL
    )
    """
)

print("Table Berhasil dibuat")