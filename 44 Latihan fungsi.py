# Latihan Fungsi

import os


def header():
    '''Fungsi Header'''
    os.system("cls")
    print(f"{'Program Menghitung Luas':^40}")
    print(f"{'Menghitung Kelilig':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''Fungsi Input User'''
    #Mengambil input user
    lebar = int(input("Masukkan nilai lebar: "))
    panjang = int(input("Masukkan nilai panjang: "))

    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''Fungsi  Luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''Fungsi Keliling'''
    return 2*(lebar+panjang)

def display(message,value):
    print(f"Hasil Perhitungan {message} = {value}")

#Program utama

while True:
    header()
    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)

    display("luas", LUAS)
    display("keliling", KELILING)

    isContinue = input("Apakah lanjut(y/n)?")
    if isContinue == "n":
        break

print("Program selesai, terima kasih")