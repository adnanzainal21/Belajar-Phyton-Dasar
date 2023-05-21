# latihan gambar perulangan

bintang =  7
count = 1


# 1.For
# dummy
for i in range(bintang) :
  
  print("*"*count)
  count += 1

print("For selesai")


# 2.while
count = 1
while True:
  print("*"*count)
  count += 1
  
  if count > bintang :
    break
  
print("while selesai")


# 3 hanya ganjil saja 
print("awal while")
count = 1
spasi = int(bintang/2)
while True :
    
  if (count%2) :
    print(" "*spasi,"+"*count)
    spasi -= 1
    count += 1
    
  else :    
    count += 1
    continue
  
  if count > bintang :
    break

print("selesai")
  