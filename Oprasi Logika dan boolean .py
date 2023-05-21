# Operasi logika dan Boolean 

# not , or , and , xor

print('=====NOT=====')
a = True
c = not a
print('Data a =',a)
print('-------not')
print('Data c =',c)

print('\n')

# OR ( jika salah satu true hasilnya true ) 
print('=====OR=====')
a = False
b = False
c = a or b
print(a,'or',b,'=',c)
print('\n')

a = False
b = True
c = a or b
print(a,'or',b,'=',c)
print('\n')

a = True
b = False
c = a or b
print(a,'or',b,'=',c)
print('\n')

a = True
b = True
c = a or b
print(a,'or',b,'=',c)

print('\n')

# And ( jika sal satunya false maka hasilnya false) 
print('=====AND=====')
a = False
b = False
c = a and b
print(a,'and',b,'=',c)
print('\n')

a = False
b = True
c = a and b
print(a,'and',b,'=',c)
print('\n')

a = True
b = False
c = a and b
print(a,'and',b,'=',c)
print('\n')

a = True
b = True
c = a and b
print(a,'and',b,'=',c)

print('\n')

# XOR ( jika salah satu true hasilnya true ) 
print('=====XOR=====')
a = False
b = False
c = a ^ b
print(a,'xor',b,'=',c)
print('\n')

a = False
b = True
c = a ^ b
print(a,'xor',b,'=',c)
print('\n')

a = True
b = False
c = a ^ b
print(a,'xor',b,'=',c)
print('\n')

a = True
b = True
c = a ^ b
print(a,'xor',b,'=',c)
