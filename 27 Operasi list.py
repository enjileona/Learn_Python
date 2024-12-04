data_angka = [1,2,3,4,5,6,2,3,1,2,4,5,3,5,3]

print(f"data angka: \n{data_angka}")

#count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_2 = data_angka.count(2)

print(f"jumlah angka 4: {jumlah_data_4}")
print(f"jumlah angka 2: {jumlah_data_2}")

#ambil posisi data (index)
data = ["ucup", "otong", "niel"]

print(f"data: {data}")

index_ucup = data.index("ucup")
index_otong = data.index("otong")

print(f"index ucup = {index_ucup}")
print(f"index otong = {index_otong}")

#mengurutkan list
print(f"data angka sebuelum sort = \n {data_angka}")
data_angka.sort()
print(f"datang angka sort = \n{data_angka}")

#balik list
data_angka.reverse()
data.reverse()
print(f"data di revers = \n{data} \n{data_angka}")
