'''default argumen'''

#def fungsi (argumen):
# def fungsi (argumen = nilai defaulnya):

#Contoh 1
def  say_hello (nama = "ganteng"):
    '''fungsi dengan default argumen'''
    print(f"Hallo {nama}")

say_hello("ucup")
say_hello()

#Contoh 2
def sapa_dia(nama, pesan = "Apa Kabar?"):
    '''fungsi dengan satu input biasa, dan satu default'''
    print(f"hai {nama}, {pesan}")

sapa_dia("dudung", "hai ganteng")
sapa_dia("otong")

#Contoh 3
def hitung_pangkat (angka, pangkat = 2):
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat = 3, angka = 5)
print(hasil)
    
#Contoh 4

def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1+input2+input3+input4
    return hasil

print(fungsi())
print(fungsi(input3=10))