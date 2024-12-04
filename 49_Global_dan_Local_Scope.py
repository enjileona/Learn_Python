## Global dan Local Scope

nama_global = "Otong" #ini variabel global

#Akses Variabel global dalam fungsi

def fungsi1():
    print(f"fungsi menampilkan {nama_global}")

fungsi1()

#Akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

#Percabangan
if True:
    print (f"if menampilkan {nama_global}")

#Variabel local scope
def fungsi2():
    nama_local = "ucup" # <- Variabel local scope

fungsi2()

#contoh 1 : penggunaan akses variabel
def say_otong():
    print(f"Hello {nama}")

nama = "Otong"
say_otong()

## Contoh 2: Merubah variabel local
angka = 0
name = "ucup"

def ubah(nilai_baru, nama_baru):
    global angka #fungsi ini mendapatkan akses merubah
    global name
    angka = nilai_baru
    name = nama_baru

print(f"sebelum {angka, name}")
ubah (10, "otong")
print(f"Sesudah {angka, name}")

### Contoh 3
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0 

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)