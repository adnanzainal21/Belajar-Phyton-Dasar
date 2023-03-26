# continue , pass , break 

# pass - > berfungsi sebagai dummy 

angka =  0 

while angka < 5 :
  angka += 1
  
  if angka == 2 : 
    pass
  
  if angka == 3 :
    print("Sudah sampai angka 3")
    continue
  
  if angka == 4 :
    print("Sudah sampai angka 4")
    break
    
  print("Sudah selesai")
  
print("Program selesai")