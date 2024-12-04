
'''Minta pengguna memasukkan sebuah angka, lalu tampilkan apakah angka 
tersebut positif, negatif, atau nol.'''

# angka = int(input("Masukkan Angka: "))

# if angka < 0:
#     print (f"Angka {angka} adalah Negatif ")
# else:
#     print (f"Angka {angka} adalah Positif ")

'''Minta pengguna memasukkan angka, 
lalu tampilkan apakah angka tersebut genap atau ganjil'''

# angka = int(input("Masukkan Angka: "))

# if angka % 2 == 0:
#     print (f"angka {angka} adalah Genap")
# else:
#     print (f"angka {angka} adalah Ganjil")

'''Minta pengguna memasukkan nilai ujian, lalu tentukan apakah mereka lulus
atau tidak. Nilai kelulusan adalah 75 atau lebih.'''

# angka = int(input("Masukkan Nilai: "))

# if angka >= 75:
#     print (f"Nilai {angka}, Kamu lulus")
# else:
#     print (f"Nilai {angka}, Kamu tidak lulus")

'''Minta pengguna memasukkan dua angka, 
lalu tampilkan mana yang lebih besar atau apakah keduanya sama.'''

# angka_1 = int(input("Masukkan angka pertama: "))
# angka_2 = int(input("Masukkan angka kedua: "))

# if angka_1 > angka_2:
#     print (f"{angka_1} lebih besar dari {angka_2}")
# elif angka_1 < angka_2:
#     print(f"{angka_2} lebih besar dari {angka_1}")
# else:
#     print (f"{angka_1} sama dengan {angka_2}")

'''Minta pengguna memasukkan usia mereka, lalu tampilkan kategori:

Anak-anak (0–12 tahun)
Remaja (13–17 tahun)
Dewasa (18–59 tahun)
Lansia (60 tahun ke atas)'''

# Usia = int(input("Masukkan Usia Anda: "))

# if Usia <= 12 and Usia >= 0:
#     print (f"Usia {Usia}, anak-anak")
# elif Usia <= 17 and Usia >= 13:
#     print (f"Usia {Usia}, Remaja")
# elif Usia <= 59 and Usia >= 18:
#     print (f"Usia {Usia}, Dewasa")
# elif Usia >= 60:
#     print (f"Usia {Usia}, Lansia")
# else:
#     print ("Masukkan angka yang benar")

# Usia = int(input("Masukkan Usia Anda: "))

# if Usia < 0:
#     print("Masukkan angka yang benar")
# elif Usia <= 12:
#     print(f"Usia {Usia} Tahun, Anak-anak")
# elif Usia <= 17:
#     print(f"Usia {Usia} Tahun, Remaja")
# elif Usia <= 59:
#     print(f"Usia {Usia} Tahun, Dewasa")
# else:  # Usia >= 60
#     print(f"Usia {Usia} Tahun, Lansia")

'''Buat program yang meminta pengguna memasukkan total belanja, 
lalu tentukan diskon berdasarkan aturan berikut:

Total belanja > 1 juta: Diskon 20%
Total belanja > 500 ribu: Diskon 10%
Total belanja ≤ 500 ribu: Tidak ada diskon
Tampilkan total yang harus dibayar setelah diskon.'''

# belanja = int(input("Total Belanja: "))

# if belanja > 1000000:
#     diskon = belanja * 20//100
# elif belanja > 500000:
#     diskon = belanja * 10//100
# else:
#     diskon = 0

# totalbayar = belanja - diskon
# print (f"diskon: {diskon}")
# print (f"Total Bayar = Rp{totalbayar}")
# print ("Silahkan membayar ke kasir")

'''Buat program sederhana yang menyimpan angka rahasia (misalnya 10). 
Minta pengguna menebak angka tersebut, lalu tampilkan apakah tebakan mereka 
terlalu kecil, terlalu besar, atau benar.'''

# tebak_angka = int(input("Tebak Angka: "))
# angka = 10

# if tebak_angka == 10:
#     print (f"Tebakan Angka = {tebak_angka}, Tebakan BENAR!")
# elif tebak_angka > 10:
#     print (f"Tebakan Angka {tebak_angka},Tebakan terlalu besar :(")
# else:
#     print (f"Tebakan Angka {tebak_angka}, Tebakan terlalu kecil :(")