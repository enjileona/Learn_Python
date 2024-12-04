#tugas

#-----0+++++5-----8+++++11-----

inputUser = float(input("Masukkan angka bernilai \n lebih dari 0 dan kurang dari 5 \n atau lebih dari 8 dan \n kurang dari 11: "))

angka1 = (inputUser > 0 and inputUser < 5)
print("Lebih dari 0 dan kurang dari 5=", angka1)

angka2 = (inputUser > 8 and inputUser < 11)
print("Lebih dari 8 dan kurang dari 11=", angka2)

isCorrect = (angka1 or angka2)
print ("Angka yang anda masukkan:", isCorrect)

#++++++0-------5+++++++8------11+++++++
print ("\n","="*10,"\n")

inputUser = float(input("Masukkan angka bernilai \n kurang dari 0 atau lebih dari 5 \n dan kurang dari 8 atau \n lebih dari 11: "))

angka1 = (inputUser < 0 or inputUser > 5)
print("Kurang dari 0 atau lebih dari 5=", angka1)

angka2 = (inputUser < 8 or inputUser > 11)
print("Kurang dari 8 atau lebih dari 11=", angka2)

isCorrect = (angka1 and angka2)
print ("Angka yang anda masukkan:", isCorrect)

