# Operator dalam bentuk methods

## Merubah case dari string

# Merubah semua ke upper case

salam = "Bro!"
print("normal = ", salam)
salam = salam.upper()
print ("upper = ", salam)

#merubah semua ke lower case
alay = "keCE AbieZzzZZ"
print("normal = ", alay)
alay = alay.lower()
print("lower = ", alay)

#Pengecekan dengan isX method

#contoh pengecekan lower dan upper case
salam = "sist"
apakah_lower = salam.islower() #hasil boolean
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() #hasil boolean
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai huruf besar

judul = "It Is Okay Not To Be Okay"
cek_judul = judul.istitle() #hasilbool
print (judul + " is title = "+ str(cek_judul))

## cek komponen startswith() dan endswith ()
cek_start = "apa kabar".startswith("apa")
print ("start = " + str(cek_start))

cek_end = "apa kabar".endswith("kabar")
print ("end = " + str(cek_end))

# penggabungan komponen join() dan split()
pisah = ["aku","sayang","kamu"]
gabungan = ",".join(pisah)
print(pisah)
print(gabungan)

gabungan = " ".join(pisah)
print(gabungan)

gabungan = " ehm ".join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

## alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")
kiri = "kiri".ljust(10)
print("'"+kiri+"'")
tengah = "tengah".center(20,"=")
print("'"+tengah+"'")

#kebalikannya <-- strip()
tengah = "tengah".strip("=") #menghilangkan tanda :
print("'"+tengah+"'")