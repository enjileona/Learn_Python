## Operasi

# index  0(-3)           , 1(-2)      ,2(-1)
data = ["sujarniel", "setiady", "Pasae"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir (index 2) = {data_terakhir}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data: {panjang_data}")

#manipulasi  data list
#menambah item pada list sesuai posisi
print(f"data sebelum ditambah: \n{data}")

data.insert(1,"enji")
print(f"data setelah ditambah: \n{data}")
 
#menambah di akhir list
data.append("leona")
print(f"ditambah lagi: \n{data}")

#menambah list dengan list
data_baru = ["makan", "apa", "ya?"]
data.extend(data_baru)
print(f"data gabungan: \n{data}")

#merubah data
#ubah data 2 menjadi "euanggay"
data[2] = "euanggay"
print(f"data rubah: \n{data}")

#meremove data
data.remove ("Pasae")
print(f"data remove: \n{data}")

#meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir: \n{data}")

#print (data_akhir)