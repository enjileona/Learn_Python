'''Fungsi dengan Argumen (input)'''

# template
# def nama_fungsi(argumen):
# #badan fungsi
 
def hello_world(nama):
    '''fungsi hello world menerima input dengan '''
    print(f"selamat datang dunia wahai {nama}")

hello_world("ucup")
hello_world("otong") 

#Program tambah
def tambah (angka1, angka2):
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah (1,2)
tambah (1000,3)

def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")

anggota_boyband = ["ucup", "otong", "dudung"]

say_hi(anggota_boyband)

