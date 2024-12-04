#Penggunaan tipe hints

import string
def sepuluh_pangkat(argument:int) ->int:
    '''Fungsi  dengan Hints'''
    output = 10*argument
    return output

HASIL = sepuluh_pangkat(4)
print(HASIL)

def display (argument:string):
    print(argument)

display("Ucup")