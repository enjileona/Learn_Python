# continue, pass, break

# pass: berfungsi sebagai dummy, tidak akan di eksekusi

angka = 0

while angka < 5:
    angka += 1

    if angka == 3:
        pass # tidak akan di eksekusi
       
    print (angka)

def fungsi():
    pass

#continue

angka = 0

print (f"angka sekarang: {angka}") # aksi 1

while angka < 5:
    angka += 1
    print (f"angka sekarang: {angka}") # aksi 2

    if angka == 3:
        print ("nice!")
        continue
    print ("apakag") #aksi 2

print ("done")
    