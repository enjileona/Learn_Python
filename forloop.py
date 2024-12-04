# for item in iterable:
    # Lakukan sesuatu dengan item

# fruits = ["Apple", "Mango", "Orange"]
# for fruit in fruits:
#     print (f"Saya suka {fruit}")

'''Fungsi range() digunakan untuk menghasilkan urutan angka.

range(n): Dari 0 hingga n-1
range(start, stop): Dari start hingga stop-1
range(start, stop, step): Dengan langkah tertentu '''

# for i in range(5):
#     print(f"Loop ke-{i}")
# print ("\n")

# for i in range(1,11,2):
#     print (f"angka {i}")
# print ("\n")

# for i in range (1,11):
#     if i%2 != 0:
#         print (i)
# print ("\n")

# text = "makan"
# for i in text:
#     print (i)

'''TABEL PERKALIAN'''

# for i in range (1,11):
#     for j in range (1,11):
#         hasil = i*j
#         print (f"{i} x {j} = {hasil}")


'''Penggunaan break dan continue
break: Menghentikan loop sepenuhnya.
continue: Melompati iterasi saat ini dan lanjut ke iterasi berikutnya.'''

# for i in range(10):
#     if i == 5:
#         break #keluar dari loop
#     print (i)

# for i in range (10):
#     if i%2 == 0:
#         continue
#     print (i)

# angka = [1, 2, 3, 4, 5]
# kuadrat = [x**2 for x in angka]
# print(kuadrat)
'''menampilkan angka 1-20'''
# for i in range (1,21):
#     print (i)

'''menampilkan angka ganjil dari 1-20'''
# for i in range(1,21):
#     if i%2==0:
#         continue
#     print (i)

'''Menghitung jumlah semua angka dari daftar: [10, 20, 30, 40].'''
# daftar = [10,20,30,40]
# print (sum(daftar))

'''Pola segiti

*
**
***
****

'''

# for i in range (1,8):
#     print (i*"*")

'''Tulis program untuk menghitung faktorial dari sebuah angka. 
Contohnya, jika angka adalah 5, maka faktorial adalah 5 * 4 * 3 * 2 * 1 = 120'''

# n = int(input("Masukkan Angka: "))
# faktorial = 1

# for i in range (1,(n+1)):
#     faktorial *=  i
# print (faktorial)

'''Latihan 1: Total Penjumlahan'''
# daftar_angka = [10, 20, 30, 40, 50]
# jumlah = 0

# for i in daftar_angka:
#     jumlah += i
# print(jumlah)

'''Latihan 2: Perkalian Semua Elemen'''
# daftar_angka = [2, 3, 5]
# perkalian = 1

# for i in daftar_angka:
#     perkalian *= i
# print(perkalian)

'''Temukan Nilai Maksimum'''
# daftar_angka = [12, 45, 7, 89, 23]
# max = daftar_angka [0]

# for angka in daftar_angka:
#     if angka > max:
#         max = angka
# print(max)

'''Temukan nilai minimum'''
# daftar_angka = [25, 15, 40, 5, 30]
# min = daftar_angka [0]

# for angka in daftar_angka:
#     if angka < min:
#         min = angka
# print (min)

'''Temukan Angka Terbesar Kedua''' #belum paham
# daftar_angka = [10, 20, 30, 40, 50]

# # Inisialisasi nilai untuk terbesar pertama dan kedua
# max1 = daftar_angka[0]
# max2 = None  # Belum diketahui

# for angka in daftar_angka:
#     if angka > max1:  # Jika ditemukan angka lebih besar dari max1
#         max2 = max1   # max2 menjadi max1 sebelumnya
#         max1 = angka  # Perbarui max1 dengan angka saat ini
#     elif max2 is None or angka > max2:  # Jika angka lebih besar dari max2
#         max2 = angka  # Perbarui max2

# print("Angka terbesar kedua:", max2)

'''jumlah dan rata-rata'''
# daftar_angka = [4, 8, 12, 16, 20]
# jumlah = 0

# for angka in daftar_angka:
#     jumlah += angka
# rata_rata = jumlah / len(daftar_angka)

# print (jumlah)
# print (rata_rata)

'''temukan angka genap terbesar'''
daftar_angka = [41, 7, 5, 20, 9, 31]

mx = 0
for angka in daftar_angka:
    if angka > mx and angka % 2 == 0:
        mx = angka
print (f"genap terbesar {mx}")

mn = float("inf")
for angka in daftar_angka:
    if angka < mn and angka % 2 != 0:
        mn = angka
print (f"ganjil terkecil {mn}")

'''Soal 5: Hitung Frekuensi Angka Tertentu'''
# daftar_angka = [2, 7, 3, 2, 5, 3, 7, 2]
# # angka_dicari = 2
# existing_number = [2,7,3,5]


# for number in existing_number:
#     frekuensi = 0
#     for angka in daftar_angka:
#         if angka == number:
#             frekuensi += 1
#     print (frekuensi)


# daftar_angka = [2, 7, 3, 2, 5, 3, 7, 2]
# existing_number = []

# for angka in daftar_angka:
#     if not(angka in existing_number):
#         existing_number.append(angka)

# for number in existing_number:
#     frekuensi = 0
#     for angka in daftar_angka:
#         if angka == number:
#             frekuensi += 1
#     print (f"{number} ada {frekuensi} kali")



#daftar_angka = [10, 20, 30, 40, 50]

#angka = 7
# max1 = daftar_angka[0] # 7
# max2 = 0 #5

# for angka in daftar_angka:
#     if angka > max1:
#         max2 = max1
#         max1 = angka
#     elif angka > max2 and max1 != angka :
#          max2 = angka
# print (f"terbesar kedua: {max2}")

# min1 = daftar_angka[0]
# min2 = float("inf")

# for angka in daftar_angka:
#     if angka < min1:
#         min1 = angka
# print (f" terkecil: {min1}")

# for angka in daftar_angka:
#     if angka < min1:
#         min2 = min1
#         min1 = angka
#     elif angka < min2 and min1 != angka:
#         min2 = angka
# print (f"terkecil kedua: {min2} ")