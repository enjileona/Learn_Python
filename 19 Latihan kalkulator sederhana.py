#latihan

#kalkulator sederna
print ("="*10)
print ("Kalkulator Sederhana")
print ("="*10)

angka_1 = (float(input ("masukkan angka_1: ")))
operator = (input ("masukkan operator (+, -, /, x): "))
angka_2 = (float(input ("masukkan angka_2: ")))

#percabangan
if operator == "+":
    hasil = angka_1 + angka_2
    print (f"hasilnya adalah: {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print (f"hasilnya adalah: {hasil}")
elif operator == "*" or operator == "x":
    hasil = angka_1 * angka_2
    print (f"hasilnya adalah: {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print (f"hasilnya adalah: {hasil}")
else:
    print("Masukkan data yang benar!")
print ("Akhir program")