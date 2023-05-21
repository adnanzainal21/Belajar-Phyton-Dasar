# bentuk method
from turtle import clear


world = "world"
print("hello " + world)

# merubah ke upper case
world = world.upper()
print("upper = " + world)

# merubah semua ke lower case
world = world.lower()
print("lower = " + world )

#isalpha() <-- untuk mengcek semunya huruf 
#isalpha() <-- huruf dan angka 
#isdecimal() <-- angka saja
#isspace() <-- spasi , tab , newline \n
#istitle() <-- semua kata dimulai dengan huruf besar

judul = "Hello Everybody Myname Is Andi Karna"

cek_judul = judul.istitle()
print(judul + "is title = " + str(cek_judul))

# cek komponnen startwith() endwith() <--keren
cek_start = "Hello world ".startswith("Hello")
print("start = " + str(cek_start))

cek_end = "Hello World".endswith("World")
print("end = " + str(cek_end))


# penggabungan komponen join() split()
pisah = ['aku' , 'sayang' , 'nova']
gabungan = ' '.join(pisah) 
print(pisah)
print(gabungan)

gabungan2 = "akueesayangeekamu"
print(gabungan2.split('ee'))

#alokasi karakter
print(5*"=" + "data" + "="*5)

#alokasi karakter rjust() ljusat() center()
kanan = "kanan".rjust(20)
kiri = "kiri".ljust(20)
center = "center".center(20,"=")

print("'"+kanan+"'")
print("'"+kiri+"'")
print("'"+center+"'")


# kebalikanya strip()
center = center.strip("=")
print("'"+center+"'")







