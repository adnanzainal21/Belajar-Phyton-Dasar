# Operasi
data = ["andi" , "karna" , "helloworld"]


# data pertama
data_0 = data[0]
print(f"data pertama index 0 = {data_0}")

# data terakhir
data_terakhir = data[-1]
print(f"data terakhir = {data_terakhir}")

# data 
data_helloworld = data[-2]
print(f"data hello world = {data_helloworld}")

# mengambil info jumlah data
panjang_data = len(data)
print(f"panjang data = {panjang_data}")


# manipulasi data list 

# menambah data di awal
data.insert(1,"python")
print(data)

# menambah data di akhir
data.append("Program")
print(data)

# menmbah list dengan list
data_baru = ["adit" , "sopo" , "jarwo" ]
data.extend(data_baru)
print(f"data gabungan =\n {data}")

# mengubah data 
data[2] = "Daniel"
print(f"data berubah =\n {data}")

# remove data 
data.remove("Daniel")
print(f"data remove =\n {data}")

# meremove data akhir
data.pop()
print(f"Data akhir = {data}")