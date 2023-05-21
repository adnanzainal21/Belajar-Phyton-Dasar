#Komparaso dan logika

#membuat gabungan area rentang dari angka 

#++++3----10++++

inputUser = float(input("Masukan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10\n="))

#+++3--------
#memeriksa angka kurang dari 3

isKurangDari = (inputUser < 3)
print("Angka Kurang dari 3 = " , isKurangDari)

#---10++++
#memeriksa angka lebih dari 10

isLebihDari = (inputUser > 10)
print("Angka lebih dari 10 = ", isLebihDari)

#++++3----10++++
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukan = ", isCorrect)

print("\n",10*'=',"\n")

inputUser = float(input("Masukan angka yang bernilai \nlebih dari 3 \natau \nkurang dari 10\n="))

#----3++++
#memeriksa angka lebih dari 3

isLebihDari = ( inputUser > 3)
print("Angka Lebih dari 3 = ", isLebihDari)

#++++10----
#memeriksa angka kurang dari 10

isKurangDari = ( inputUser < 10)
print("Angka kurang dari 10 = ", isKurangDari)

#-----3+++++10-----
isCorrect = isLebihDari or isKurangDari 
print("Angka yang anda masukan = ", isCorrect)


