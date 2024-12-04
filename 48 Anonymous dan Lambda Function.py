#Lamda Function

def f_kuadrat(angka):
    return angka**2

print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

#Lamda

#output = lamda argument : Expression

kuadrat = lambda angka : angka**2
print(f"hasil fungsi kuadrat = {f_kuadrat(5)}")

pangkat = lambda num,pow : num**pow
print(f"hasil lamda pangkat = {pangkat(5,2)}")

# Sorting untuk list biasa 
data_list = ["otong", "ucup" , "dudung"]
data_list.sort()
print(f"sorted list = {data_list}")

# Sorting pakai panjang
def panjang_nama (nama):
    return len (nama)

data_list.sort (key=panjang_nama)
print(f"sorted list by panjang = {data_list}")

#Sort pakai lambda
data_list = ["otong", "ucup", "dudung"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by lamda = {data_list}")

#Filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,13]

def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima, data_angka))
data_angka_baru = list(filter(lambda x:x<7,data_angka))
print(data_angka_baru)

#Kasus genap
data_genap = (list(filter(lambda x: (x%2 == 0), data_angka)))
print(data_genap)

#Kasus ganjil
data_ganjil = (list(filter(lambda x: (x%2 != 0), data_angka)))
print(data_ganjil)

#Kelipatan 3
data3 = (list(filter(lambda x: (x%3 == 0), data_angka)))
print(data3)


#anonymous function
#currying <- Haskell Curry

def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2)
print(f"fungsi biasa = {data_hasil}")

# dengan currying menjadi

def pangkat(n):
    return lambda angka:angka**n


pangkat2 = pangkat(2)
print(f"pangkat2 = {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"pangkat3 = {pangkat3(3)}")
print(f"pangkat bebas = {pangkat(4)(5)}")



# 2 ^ 6 + 3 ^ 2 - 2 ^ 3 = ?

def pangkat(angka,n):
    hasil = angka**n
    return hasil


def operasi():
    hasil = pangkat(2,6)+pangkat(3,2)-pangkat(2,3)
    return hasil

print (operasi())

# 4 ^ 4 ^ 4

hasil = pangkat((pangkat(4,4)),4)
print(hasil)

# nama saya niel dan saya ganteng
# nama saya enji dan saya canti

def perkenal (nama,look):
    bb = (f"nama saya {nama} dan saya {look}")
    return bb

print(perkenal("niel","ganteng"))
print(perkenal("enji","canti"))
