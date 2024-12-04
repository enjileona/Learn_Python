# Width and multiline

# data

data_nama = "niel"
data_umur = 12
data_tinggi = 170 
data_nomor_sepatu = 50

#string standar
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_nomor_sepatu}"

print(5*"="+"DATA STRING"+"="*5)
print(data_string)

#string multiline (menggunakan entar, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur},\ntinggi = {data_tinggi}, \nnomor sepatu = {data_nomor_sepatu}"

print(5*"="+"DATA STRING"+"="*5)
print(data_string)

#string multiline (kutip triplets)
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
nomor sepatu = {data_nomor_sepatu}"""

print(5*"="+"DATA STRING"+"="*5)
print(data_string)

#mengatur lebar
data_nama = "niel"
data_string = f"""
nama = {data_nama:>5}
umur = {data_umur:>5}
tinggi = {data_tinggi:>5}
nomor sepatu = {data_nomor_sepatu:>5}"""

print(5*"="+"DATA STRING"+"="*5)
print(data_string)