#  Konversi Satuan Temperatur

# Celsius ke satuan lain
print("\nPROGRAM TEMPERATUR\n")

celcius = float(input('Masukan suhu dalam celsius : '))
print("Suhu celsius = ",celcius, "Celcius")

# reamur 
reamur = (4/5) * celcius
print("Suhu reamur = ", reamur,"Reamur")

# fahrenheit
farenheit = ((9/5) * celcius) + 32
print("Suhu Farenheit = ",farenheit, "Farenheit")
    
# Kelvin
kelvin = celcius + 273
print("Suhu kelvin = ",kelvin, "Kelvinr")

