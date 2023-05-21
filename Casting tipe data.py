# Merubah dari satu tipe ke tipe lain

#Integer
print("=====INTEGER=====")

data_int    = 9
print("data = ", data_int, "type : ", type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int) # akan false jika nilai int 0

print("data = ", data_float, "type : ", type(data_float))
print("data = ", data_str, "type : ", type(data_str))
print("data = ", data_bool, "type : ", type(data_bool))

##Float
print("=====FLOAT=====")

data_float  = 9.5
print("data = ", data_float, "type : ", type(data_float))

data_int  = int(data_float) # data akan di bulat kan ke bawah
data_str  = str(data_float)
data_bool = bool(data_float) 

print("data = ", data_int, "type : ", type(data_int))
print("data = ", data_str, "type : ", type(data_str))
print("data = ", data_bool, "type : ", type(data_bool))

##Boolean
print("=====BOOLEAN=====")

data_bool   = False
print("data = ", data_bool, "type : ", type(data_bool))

data_int   = int(data_bool)
data_str   = str(data_bool)
data_float = float(data_bool)

print("data = ", data_int, "type : ", type(data_int))
print("data = ", data_str, "type : ", type(data_str))
print("data = ", data_float, "type : ", type(data_float))

##String
print("=====String=====")

data_str    = "10" # data string bisa dirubah jika dimasukan angka
print("data = ", data_str, "type : ", type(data_str))

data_int   = int(data_str)
data_bool  = bool(data_str)
data_float = float(data_str)

print("data = ", data_int, "type : ", type(data_int))
print("data = ", data_bool, "type : ", type(data_bool))
print("data = ", data_float, "type : ", type(data_float))
