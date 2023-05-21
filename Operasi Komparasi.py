# Operasi Komperasi

# Setiap hasil dari komperasi adalah boolean

# > , < , > = , <= , == , != , is , is not

a = 4
b = 2

# lebih besar dari 
print("=====Lebih besar dari=====")
hasil = a > 2
print(a, '>', 2 , '=' , hasil)
hasil = b > 2
print(b, '>', 2 , '=' , hasil)
hasil = b > 2
print(b, '>', 3 , '=' , hasil)

# lebih besar dari sama dengan
print("=====Lebih besar dari sama dengan=====")
hasil = a >= 3
print(a, '>=', 3 , '=' , hasil)
hasil = b >= 3
print(b, '>=', 3 , '=' , hasil)
hasil = b >= 2
print(b, '>=', 2 , '=' , hasil)

# kurang besar dari sama dengan
print("=====Lebih besar dari sama dengan=====")
hasil = a <= 3
print(a, '<=', 3 , '=' , hasil)
hasil = b <= 3
print(b, '<=', 3 , '=' , hasil)
hasil = b <= 2
print(b, '<=', 2 , '=' , hasil)

# Sama dengan ( == )
print("=====Sama dengan=====")
hasil = a == 4
print(a, '==', 4 , '=', hasil)
hasil = b == 4
print(a, '==', 4 , '=', hasil)

# tidak sama dengan ( != )
print("=====Tidak Sama dengan=====")
hasil = a != 4
print(a, '!=', 4 , '=', hasil)
hasil = b != 4
print(a, '!=', 4 , '=', hasil)

print("\n")

# komperasi object identity ( is )
x = 5 # ini adalah assigment membuat object
y = 5 
print('nilai x =',x ,'id, =',hex(id(x)))
print('nilai y =',y ,'id, =',hex(id(y)))
hasil = x is y
print('x is y = ',hasil)

print("\n")
x = 10 # ini adalah assigment membuat object
y = 5 
print('nilai x =',x ,'id, =',hex(id(x)))
print('nilai y =',y ,'id, =',hex(id(y)))
hasil = x is y
print('x is y = ',hasil)
