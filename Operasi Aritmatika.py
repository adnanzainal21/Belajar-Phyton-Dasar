# Operasi Aritmatika

a = 10
b = 3

# Operasi Tambah
hasil = a + b
print(a,'+',b,'=', hasil)

# Operasi Kurang
hasil = a - b
print(a,'-',b,'=', hasil)

# Operasi bagi
hasil = a / b
print(a,'/',b,'=', hasil)

# Operasi Perkailan
hasil = a * b
print(a,'*',b,'=', hasil)

# Operasi Eksponen(Pangkat)
hasil = a ** b
print(a,'**',b,'=', hasil)

# Operasi modulus ( Sisa bagi )
hasil = a % b
print(a,'%',b,'=', hasil)

# Operasi flor division ( Pembulatan)
hasil = a // b
print(a,'//',b,'=', hasil)

# Prioritas Operasi 
x = 3
y = 2
z = 4

# Urutan prioritas () , eksponen , perkalian , pertambahan
hasil = x ** y * z + x / y - y % z // x 
print(x,"**", y,"*", z,"+", x,"/", y,"-", y, "%",z, "//",x, "=", hasil )

hasil = ( x + y ) / z
print("(",x,"+",z,")","/",z,"=",hasil)