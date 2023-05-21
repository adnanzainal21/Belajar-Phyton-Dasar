# a = 10 , a adalah variable dengan nilai 10

# Tipe data : Angka satuan ( Integer )
data_integer = 1
print("Data : ", data_integer)
print("- bertipe : ", type(data_integer))

# Tipe data ; Float
data_float = 1.5
print("Data float : ", data_float)
print("- bertipe : ", type(data_float))

# Tipe data : kumpulan karakter ( String )
data_string = " Hello World "
print("Data String : ", data_string)
print("- bertipe : ", type(data_string))

# Tipe data : Biner/false ( Boolean )
data_boolean = False
print("Data Boolean : ", data_boolean)
print("- bertipe : ", type(data_boolean))

## Tipe data khusus

# bilangan khusus
data_complex = complex(5,6)
print("Data : ", data_complex)
print("- bertipe : ", type(data_complex))

# Tipe data dari bahasa C

from ctypes import c_double, c_char

data_c_double = c_double(5,5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))