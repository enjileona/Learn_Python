# Fungsi Return

#Template fungsi dengan kembalian
# def fungsi(argumen):
#   badan fungsi
#   return output

#fungsi kuadrat

def kuadrat (input_angka):
    '''Fungsi Kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat

y = kuadrat(5)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print (z)