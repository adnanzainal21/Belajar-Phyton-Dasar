from turtle import clear
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "usershop",   
)

cursor = db.cursor()

query = "INSERT INTO barang(nama, harga, stok) VALUES(%s, %s, %s)"

print("Masukan nama barang : ")
nmBarang = input()
print("Masukan Harga Barang : ")
harga = input()
print("Masukan Jumlah Stok Terakhir : ")
stok = input()

clear()

data =  (nmBarang,harga,stok)

cursor.execute(query,data)

db.commit()
print("Data Berhasil di input!!")
