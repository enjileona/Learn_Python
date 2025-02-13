#Format String

#contoh generic

#string
nama = "niel jelek"
format_str = f"halo {nama}"
print (format_str)

#boolean
boolean = False
format_str = f"boolean = {boolean}"
print (format_str)

#angka
angka = 2005.5
format_str = f"angka = {angka}"
print (format_str)

#bilangan bulat
angka = 15
format_str = f"Bilangan bulat = {angka:d}"
print (format_str)

#bilangan dengan ordo ribuan
angka = 2000
format_str = f"ribuan = {angka:,}"
print (format_str)

#bilangan desimal
angka = 2005.38484
format_str = f"desimal = {angka:.2f}"
print (format_str)

#menampilkan leading zero
angka = 2005.38484
format_str = f"desimal = {angka:08.2f}"
print (format_str)

#menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.54
format_minus = f"minus = {angka_minus:-d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print (format_plus)

#memformat persen
persentase = 0.045
format_persen = f"persentase={persentase:.2%}"
print (format_persen)

#melakukan operasi aritmatika dalam placeholder
harga  = 10000
jumlah = 5

format_string = f"harga total = Rp. {jumlah*harga:,}"
print(format_string)

#format angka lain (binari, octal, hexadecimal)

angka = 225
format_binari = f"binari = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexadecimal = f"hexadecimal = {hex(angka)}"

print(format_binari)
print(format_octal)
print(format_hexadecimal)


