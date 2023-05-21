# kalkulator

angka1 = float(input("Masukan angka pertama = "))
operator = input("operator ( + , - , x  , / ) : ")
angka2 = float(input("Masukan angka kedua = "))

# percabangan

if operator == "+" :
  print(f"hasil dari Penjumlahan = {angka1 + angka2}")
    
elif operator == "-" :
  print(f"hasil dari Pengurangan = {angka1 - angka2}")
  
elif operator == "x" :
  print(f"hasil dari Perkalian = {angka1 * angka2}")
  
elif operator == "/" :
  print(f"hasil dari Permbagian = {angka1 // angka2}")

print("Done")