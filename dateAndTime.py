# Date and time

import datetime as dt 

tanggal_sekarang = dt.date.today()
tanggal_lahir = dt.date(2001,3,19)

print(f"tanggal = {tanggal_sekarang}")
print(f"hari ini = {tanggal_sekarang:%A}")
print(f"tanggal lahir = {tanggal_lahir}")

print("Silahkan Masukan tanggal lahir")

tanggal = int(input("tanggal : " ))
bulan = int(input("bulan : " ))
tahun = int(input("tahun : " ))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir kamu = {tanggal_lahir}")

x = tanggal_sekarang - tanggal_lahir
umur = x.days // 365
print(f"Umur kamu sekarang {umur} tahun")