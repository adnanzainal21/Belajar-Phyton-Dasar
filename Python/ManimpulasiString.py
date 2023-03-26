# mengabungkan string
nama_depan = "Andi"
nama_belakang = "karna"
nama_lengkap = nama_depan + nama_belakang
print(nama_lengkap)

# menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))


# operator untuk string

d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " +  str(status))


# mengulang string 
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-2 : " + nama_lengkap[2])
print("index ke-3 : " + nama_lengkap[3])
print("index ke-[4:7] : " + nama_lengkap[4:9])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))

# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))

data = "Hello World"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))











